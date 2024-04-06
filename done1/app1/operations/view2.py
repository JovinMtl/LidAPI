from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser


from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
# from django.dispatch import receiver
# from django.db.models.signals import post_save
# from rest_framework.authtoken.models import Token
from django.http import request as requeste
# from django.db.models.query import QuerySet.DoesNotExist
from datetime import datetime, timedelta
from django.utils import timezone
from functools import wraps
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import json

from ..serializers import RequeSeria, UserSeriazer, PorteSeria
from ..serializers import InveSeria, DepoSeria, SoldeSeria, OperationSeria,\
                            BasicInfoSeria, RetraiSeria, CommissionSeria, \
                            PoolUserSeria
from ..models import Requeste, PorteFeuille, Recharge, Differente,\
                    Trade, DepotPreuve, RetraitLives, InvestmentsMade,\
                    Solde, OperationStore, CommissionForWithdrawal,\
                    InterestRateForInvestment, PoolUser

from ..lumi.client_Lumi import LumiRequest 
from ..lumi.login import UserBrowising
from .code_transanction import GenerateCode




class RequeWithdrwawViewSet(viewsets.ViewSet):
    """This is for Managing the Requestes"""
  
    def list(self, request):
        """For listing all available requestes"""
        queryset = Requeste.objects.filter(state_progress__lte=1)
        # queryset = Requeste.objects.all()
        serializer_class = RequeSeria(queryset, many=True)
        return Response(serializer_class.data)
    
    def _checkBalance(self, user, amount):
        """This is for checking whether we have that amount to 
        give our user before Uploading his funds to Lumicash.
        
        If we do not have sufficient funds, then we need to acquire it
        in order to serve the customer."""
        if user.lumicash >= int(amount):
            return 200
        else:
            return 201
    def create(self, request):
        """For creating new requestes
        for what? 
        """
        company_portefeuille = PorteFeuille.objects.get(owner__username='muteule')
        link = "no link"
        # user_agent = request.META.get('HTTP_USER_AGENT')
        data_sent = request.data
        username = data_sent['username']
        user_password = data_sent['password']
        auth = authenticate(request, username=username,\
                             password=user_password)
        if not data_sent['amount_to_deb'] and (data_sent['amount_to_send'] and auth):
            #requesting to get fund
            user = User.objects.get(username=username)
            print(f"You last logged in at: {auth}")
            new_request = Requeste.objects.create(user_id=user)
            new_request.amount_to_send = data_sent['amount_to_send']
            new_request.receiver_number = data_sent['receiver_number']
            # new_request.user_id = user
            new_request.user_username = user.username
            new_request.state_progress = 1
            url = f"http://127.0.0.1:8002/jov/api/reque//{new_request.id}/approve/"
            new_request.link_to_activate = url
            request_serializer = RequeSeria(new_request, context={'request': request})
            if request_serializer.is_valid:
                print("You are ready to go")
                new_request.save()
                return Response(request_serializer.data)

            print(f"Your request is about:\n{new_request.amount_t_cred}")
            return JsonResponse({"You are authenticated": username})
        if data_sent['amount_to_deb'] and auth:
            #user wants to upload to Lde
            #requesting to withdraw lumicash and get Lde
            # lumi = LumiRequest()
            print(f"You want to give Lumicash and get Lde")
            amount_to_deb = data_sent['amount_to_deb']
            has_balance = self._checkBalance(company_portefeuille,\
                                              amount_to_deb)
            if has_balance == 201:
                print(f"the balance is : {has_balance}")
                return JsonResponse({"We don't have":"Enough Funds"})
            if has_balance == 200:
                print(f"the balance is again : {has_balance}")
                code = GenerateCode()
                # code_transaction = code.generate('recharge')
                code_transaction = code.gene()
                print(f"You are about to use code:  {code_transaction}")
                new_recharge = Recharge.objects.create(\
                    owner=auth, phone=data_sent['number_to_deb'],\
                    amount=amount_to_deb,
                    code_transaction=code_transaction)
                lumi = UserBrowising(\
                    amount_to_send=amount_to_deb\
                        ,user_to_pay=data_sent['number_to_deb'],
                        code_transaction=code_transaction)
                response = lumi.askFund()
                # print(f"From Lumicash : {response.json()}")
                if response.status_code == 200:
                    new_recharge.save()
                    link = response.json().get('link_activate')
                    benefitor_portefeuille = PorteFeuille.objects.get(\
                        owner=auth)
                    # print(f"\nCelui ci: {benefitor_portefeuille} aura argent\n")
                    
                return JsonResponse({f"Hello '{username.upper()}', Your request is waiting for your \
    approval. please copythe link below and paste it in the browser to finish":\
                                    link })
        
    def _retranche(self, source, destination, amount, pay_method=1):
        """THis function retrieves the amount """
        response = {
                    'code_status': 203,
                    'source' : source,
                    'destination': destination,
                }
        if pay_method == 1:
            #lumicash
            if int(source.lumicash) >= int(amount):
                print(f"La source au Debut: {source.lumicash}")
                source.lumicash -= int(amount)
                destination.lumicash += int(amount)
                source.save()
                destination.save()
                print(f"La source a la Fin: {source.lumicash}")
                print(f"avec montant: {amount}")
                response['code_status'] = 200
                return response
            else:
                response['code_status'] = 201
                return response
        if pay_method == 2:
            #Lid
            if float(source.lid) >= float(amount):
                print(f"The source Begin: {source.lid}")
                source.lid -= float(amount)
                destination.lid += float(amount)
                source.save()
                destination.save()
                print(f"The source end: {source.lid}")
                print(f"The amount was : {amount}")
                response['code_status'] = 200
                return response
            else:
                response['code_status'] = 201
                return response
        if pay_method == 3:
            #mpesa
            if float(source.mpesa) >= float(amount):
                print(f"The source Begin: {source.lid}")
                source.mpesa -= float(amount)
                destination.mpesa += float(amount)
                source.save()
                destination.save()
                print(f"The source end: {source.mpesa}")
                print(f"The amount was : {amount}")
                response['code_status'] = 200
                return response
            else:
                response['code_status'] = 201
                return response
        #saving the state of compte
        # source.save()
        return response
    
    @action(methods=['post'], detail=False)
    def notOwner(self, request):
        print(f"So, you're not the owner:")
        data_sent = json.loads(request.body)
        print(f"You want to give Lumicash and get Lde, {data_sent}")
        amount_to_deb = data_sent.get('amount_to_deb')
        username = request.user
        auth = authenticate(username=username,\
                             password=data_sent.get('password'))
        company_portefeuille = PorteFeuille.objects.get(\
            owner__username='muteule')
        username = str(username)
        print(f"{username} wants to send : {amount_to_deb}")
        has_balance = self._checkBalance(company_portefeuille,\
                                            amount_to_deb)
        if has_balance == 201:
            print(f"the balance is : {has_balance}")
            return JsonResponse({"We don't have":"Enough Funds"})
        if has_balance == 200:
            print(f"the balance is again : {has_balance} at {auth}")
            code = GenerateCode()
            # code_transaction = code.generate('recharge')
            code_transaction = code.gene()
            print(f"You are about to use code:  {code_transaction}")
            new_recharge = Recharge.objects.create(\
                owner=auth, phone=data_sent['number_to_deb'],\
                amount=amount_to_deb,
                code_transaction=code_transaction)
            lumi = UserBrowising(\
                amount_to_send=amount_to_deb\
                    ,user_to_pay=data_sent['number_to_deb'],
                    code_transaction=code_transaction)
            response = lumi.askFund()
            # print(f"From Lumicash : {response.json()}")
            if response.status_code == 200:
                new_recharge.save()
                link = response.json().get('link_activate')
                benefitor_portefeuille = PorteFeuille.objects.get(\
                    owner=auth)
                # print(f"\nCelui ci: {benefitor_portefeuille} aura argent\n")
                
            return JsonResponse({f"Hello '{username.upper()}', Your request is waiting for your \
approval. please copythe link below and paste it in the browser to finish":\
                                link })
        return JsonResponse({"You are about to": "give away your lumicash"})
    
    @action(methods=['get'], detail=True)
    def approve(self, request, pk):
        if not request.user.is_authenticated:
            return JsonResponse({"You need to authenticate": "first"})
        obj = Requeste.objects.get(pk=pk)
        if obj.state_progress > 1 :
            return JsonResponse({"THis link has expired": "Please"})
        sender = obj.user_username
        try:
            sender_portefeuille = \
            PorteFeuille.objects.get(owner_username=sender)
            company_portefeuille = \
            PorteFeuille.objects.get(owner_username='muteule')
        except PorteFeuille.DoesNotExist:
            return JsonResponse({f"{sender}":f"n'a pas de portefeuille"})
        else:
            print(f"The portefeuille found: {sender_portefeuille}")
            #hageze ko tuyakura kuri portefeuille yiwe
        response_retranche = self._retranche(sender_portefeuille,\
                                              obj.amount_to_send,\
                                            company_portefeuille,\
                                                  obj.pay_method,\
                                            )
        if response_retranche == 200:
            print(f"La reponse est : {response_retranche}")
            return JsonResponse({f"Le solde de {sender}":"a ete touche"})
        elif response_retranche == 201:
            return JsonResponse({f"{sender}":"n'a pas de balance suffisant"})
        obj.date_approved = datetime.now()
        obj.state_progress = 2
        obj.approved_by = str(request.user)
        lumi = LumiRequest(obj.receiver_number, obj.amount_to_send)
        transfer_response = lumi.mySolde('transfer')
        if transfer_response.status_code == 200:
            obj.save()
        obj_serializer = RequeSeria(obj)
        if obj_serializer.is_valid:
            print(f"The user who activates is : {request.user.is_authenticated}")
            print(f"From Lumicash: {transfer_response}")
            return Response(obj_serializer.data)
        print(f"The obj to work on is : {pk}")
        return JsonResponse({"Hello": "username"})
    
    @action(methods=['post'], detail=False)
    def answer(self, request):
        """Receive the feedback from the server after the 
        approval of fund payment made by the owner.
        
        will receive the phone number sent to debit, the amount, and
        the status code(25 if it were successfully).
        The we call the self._retranche() function to do accordingly in
        the local Portefeuille."""

        
        company_portefeuille = PorteFeuille.objects.get(\
        owner_username='muteule')
        data_sent = request.POST
        phone = data_sent['phone_number']
        code_transaction = data_sent['code_transaction']
        amount = data_sent['amount']
        try:
            obj = Recharge.objects.get(code_transaction=code_transaction)
        except Recharge.DoesNotExist:
            return JsonResponse({"The Transaction code ":"Does match"})
        else:
            benefitor_portefeuille = PorteFeuille.objects.get(\
                owner=obj.owner)
            operation = self._retranche(company_portefeuille,\
                            benefitor_portefeuille, obj.amount)
            if operation['code_status'] == 200:
                print(f"{operation['source'].owner} diminue :\
{operation['source'].lumicash}")
                print(f"{operation['destination'].owner} augmente  :\
{operation['destination'].lumicash}")
            print(f"{phone}, code: {code_transaction}")
        return JsonResponse({"Server 1":"has received a reply"})
    
    
    @action(methods=['post'], detail=False)
    def trade(self, request):
        """This is for trading"""
        company_portefeuille = PorteFeuille.objects.get(\
            owner_username='muteule')
        data_sent = request.POST
        username = data_sent.get('username')
        password = data_sent.get('password')
        amount = float(data_sent.get('give'))
        
        user = authenticate(username=username, password=password)
        if user:
            portefeuilleBene = PorteFeuille.objects.get(\
                owner_username=username)
            tradeToday = Trade.objects.last()
            tauxLid = float(tradeToday.sell.lid)
            tauxLum = float(tradeToday.buy.lumicash)
            tauxMpe = float(tradeToday.buy.mpesa)
            if (data_sent.get('wantLid') == 'True') and \
                (data_sent.get('useMpe') != 'True')and (amount > 400):
                taux = float(tradeToday.sell.lid)
                result = amount / taux
                ope_lumicash = self._retranche(portefeuilleBene,\
                                 company_portefeuille, amount,\
                                     pay_method=1 )
                if ope_lumicash['code_status'] == 200:
                    print(f"money sent successfully")
                    ope_lid = self._retranche(company_portefeuille,\
                                    portefeuilleBene, result,
                                    pay_method=2)
                    if ope_lid['code_status'] == 200:
                        print(f"Client has gotten Lid")
                        return JsonResponse(\
                            {"You have gotten Lid at":f"{taux}"})
                else:
                    print(f"Lumicash wasn't send. reason: \
                          {ope_lumicash}")
                print(f"You get {result}, \
                      {portefeuilleBene.owner_username}")
                return JsonResponse({"on  you get": "done"})
            
            elif (data_sent.get('wantLum') == 'True') and \
                (data_sent.get('useMpe') != 'True') and \
                    (amount > tauxLid):
                taux = tradeToday.buy.lid
                result = amount * taux
                ope_lid = self._retranche(portefeuilleBene, \
                                          company_portefeuille, \
                                            amount=amount,\
                                                pay_method=2)
                if ope_lid['code_status'] != 200:
                    return JsonResponse({"You Lid wasn't":"Touched"})
                # print("Your Lid was sent")
                ope_lumicash = self._retranche(company_portefeuille,\
                                               portefeuilleBene,\
                                                amount=result,\
                                                    pay_method=1)
                if ope_lumicash['code_status'] != 200:
                    return JsonResponse({"You haven't gotten":"Lum"})
                # print("You have gotten new Lum")
                return JsonResponse({"You want":f"The Lum at {taux}"})
            
            elif (data_sent.get('wantMpe') == 'True') and (amount > 1.0):
                # tauxLid = tradeToday.sell.lumicash
                tauxMpe = float(tradeToday.buy.mpesa)
                result = amount * tauxMpe
                ope_lid = self._retranche(portefeuilleBene,\
                                           company_portefeuille,\
                                        amount=amount,\
                                            pay_method=2)
                if ope_lid['code_status'] != 200:
                    return JsonResponse({"Your Lid wasn't":"Touched"})
                ope_mpe = self._retranche(company_portefeuille, \
                            portefeuilleBene, amount=result,\
                                pay_method=3)
                if ope_mpe['code_status'] != 200:
                    return JsonResponse({"Your MPesa wasn't":"Touched"})
                print(f"You have new Mpesa")
            
            elif (data_sent.get('wantLid') == 'True') and \
                 (data_sent.get('useMpe') == 'True') and \
                      (amount > tauxMpe):
                taux = float(tradeToday.buy.mpesa)
                result = amount / taux
                ope_mpe = self._retranche(portefeuilleBene, \
                            company_portefeuille, \
                                amount=amount,\
                                    pay_method=3)
                if ope_mpe['code_status'] != 200:
                    return JsonResponse({"Your MPesa wasn't":"Touched"})
                ope_lid = self._retranche(company_portefeuille, \
                                          portefeuilleBene,\
                                            amount=result,\
                                                pay_method=2)
                if ope_lid['code_status'] != 200:
                    return JsonResponse({"Your Lid wasn't":"Touched"})
                print(f"You want to get  back from Mpesa")
                
            else:
                return JsonResponse({"You don't want":"The lid"})
        else:
            print(user)
            return JsonResponse({"user not connected":"Try again"})
        return JsonResponse({"For now":"It has ended well"})
          



def check_len_REST(func):
    """I want to chech the arguments of the function that
    their username is longer than 6 caracters"""
    @wraps(func)
    def inner(*args, **kwargs):
        user_agent = args[1].META.get('HTTP_USER_AGENT')
        print(f"You are at: {user_agent}")
        result = HttpResponse("Maybe your password is short or empty")
        if len (args[1].data['password']) > 6:
            jove = "THierry"
            result = func(*args, **kwargs, jove=args[1].data)
            print(f"The username is : {args[1].data}\n\n\
                  and Result: {result}")
            # kwargs['request'] = args[1].data
            return result
        else:
            print(f"The length of password is \
                  {len(args[1].data['username'])}")
            return result
    return inner



class ManageUser(APIView):
    """This is for retrieving and creating users"""
    def get(self, request):
        """THis is to view the users we have"""
        queryset = User.objects.all()
        dataSer = UserSeriazer(queryset, many=True)
        # if dataSer.is_valid():
        #     return JsonResponse({'data': dataSer.data})
        # else:
        #     return JsonResponse({"Data":"not serialized"})
        return Response(dataSer.data)

    @check_len_REST
    def post(self, request, jove):
        """This is when we want to add a new user"""

        # print(f"We want to see something:\
        #        {request.META.get('HTTP_USER_AGENT')}")
        # user_agent = request.META.get('HTTP_USER_AGENT')
        sent_data = jove
        username = sent_data['username']
        password = sent_data['password']
        print(f"Your username is: {username}")
        # return JsonResponse({"The answer is ":"No"})
        new_user = User.objects.create(username=username)
        new_user.set_password(password)
        token, created = Token.objects.get_or_create(user=new_user)
        new_portefeuille = PorteFeuille.objects.create(\
            owner = new_user)
        new_portefeuille.owner_username = new_user.username
        new_user_seriazer = UserSeriazer(new_user)
        new_porte_seriazer = PorteSeria(new_portefeuille)
        if new_user_seriazer.is_valid and new_porte_seriazer.is_valid:
            new_user.save()
            new_portefeuille.save()
            print("All is Okay")
            data = {
                'user': new_user_seriazer.data,
                'portefeuille': new_porte_seriazer.data,
            }
        return Response(data)


class UserManViewset(viewsets.ViewSet):
    """THis is for quering about the User"""
    
    @action(methods=['post'], detail=False)
    def isUserNew(self, request):
        data_sent = request.body
        decoded_data = json.loads(data_sent)
        username = decoded_data.get('username')
        another = "another"
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            print(f"The username: {data_sent} is totally new\
                  or {username}")
            return JsonResponse({"The username is":"new"}, status=200)
        else:
            if user:
                print(f"The User {user} is already registered")
                return JsonResponse({"The User":"exist"}, status=201)
        return JsonResponse({"Ended":"well"})
    
      
    # @api_view(['POST', 'GET'])
    @action(methods=['post'], detail=False)
    def injira(self, request):
        """This is for logging in and out the user"""
        print(f"First, Our visitor is : {request.user}")
        username = "None"
        password = "None"
        user_agent = request.META.get('HTTP_USER_AGENT')
        if "Mozilla" in user_agent:
            print(f"You are sendind request from the browser")
            data_sent = json.loads(request.body)
            username = data_sent.get('username')
            password = data_sent.get('password')
        else:
            sent_data = request.POST
            username = request.POST.get('username')
            password = sent_data['password']

        user = authenticate(username=username, password=password)
        if user :
            login(request, user)
            print(f"The jov : {user.username}")
            return JsonResponse({"Login successful": "without Token"})
        else:
            print(f"You need to provide a user: {user}\
                with request: {request.POST}")
            return JsonResponse({'message': 'Login failed'}, status=401)
    
    @action(methods=['get', 'post'], detail=False, \
            permission_classes= [IsAuthenticated])
    def isLoggedin(self, request):
        sent_cookies = request.COOKIES
        sent_username = sent_cookies.get('username')
        # isAdmin = 
        print(f"Our visitor is : {request.user}")
        if request.user.is_authenticated:
            isAdmin = request.user.is_superuser
            return JsonResponse({f"{request.user}": 'is authenticated',
                                 f"is_Admin": isAdmin}
                                )
        else:
            return JsonResponse({f"{request.user}": 'is not authenticated'})
            return JsonResponse({'message': 'User is not authenticated'},\
                                status=401)
## Global Functions
def writeOperation(code, source, destination, amount, currency,\
                      who_approved, motif='Depot', charge=0):
    """THis one is responsible for recording every action approved
    by the admin"""
    newOperation = OperationStore.objects.create()
    newOperation.code = code
    newOperation.source = source
    newOperation.destination = destination
    newOperation.amount = amount
    newOperation.currency = currency
    newOperation.charge = charge
    newOperation.motif = motif
    newOperation.who_approved = who_approved
    newOperation.save()
    return 200


def workOnSolde(source, destination, amount, currency, who_approved,\
                motif='Depot' ,charge=0):
    """THis is for DEPOSIT"""
    lower_currency = currency.lower()  # is sent from Vue3 in uppercase
    
    if amount > 0 and (getattr(source, lower_currency) > amount):
        destination_value = (getattr(destination, lower_currency)) + amount
        if not charge:
            source_value = (getattr(source, lower_currency)) - amount
        else:
            #source ndayikurako yose, destination ikaronka, hamwe na charge
            commission_actual = CommissionForWithdrawal.objects.last()
            commission = int(((str(getattr(commission_actual, lower_currency))).split('/'))[0])
            source_value = (getattr(source, lower_currency)) - (amount + commission)
            produit_user_account = User.objects.get(username='PRODUIT')
            produit_solde_account = Solde.objects.get(owner=produit_user_account)
            lid_produit = int((getattr(produit_solde_account, lower_currency)) + commission)
            setattr(produit_solde_account, lower_currency, lid_produit)
            produit_solde_account.save()

        setattr(source, lower_currency, source_value)
        setattr(destination, lower_currency, destination_value)

        print("The source sent is :", source.owner.username)

        responseCode = GenerateCode().giveCode()
        print("The new Code generated is : ", responseCode)
        responseOperation = writeOperation(code=responseCode, source=source.owner.username,\
                        destination=destination.owner.username, amount=amount, \
                       currency=currency,motif=motif, who_approved=who_approved, \
                        charge=charge)
        # responseOperation = 200
        if responseOperation == 200:
            destination.save()
            source.save()
            return 200
        else:
            return 203
    else :
        return 204

def workOnSoldeInve(source, destination, amount, currency, who_approved,\
                 number, invest_objet, motif='Investissement'):
    """THis is for DEPOSIT"""
    lower_currency = currency.lower()  # is sent from Vue3 in uppercase
    
    if amount > 0 and (getattr(source, lower_currency) > amount):

        try:
            invest_plan = \
                InterestRateForInvestment.objects.get(number_month=number)
        except  InterestRateForInvestment.DoesNotExist:
            return f"That plan of {number} months does not exist."
        else:
            taux = invest_plan.taux
            interest = (taux / 100) * amount * (number/12) #simple
            accumulated = amount + interest
        
        source_value = (getattr(source, lower_currency)) - amount
        
        setattr(source, lower_currency, source_value)
        setattr(destination, lower_currency, accumulated)

        print("The source sent is :", source.owner.username)

        responseCode = GenerateCode().giveCode()
        print("The new Code generated is : ", responseCode)
        responseOperation = writeOperation(code=responseCode, source=source.owner.username,\
                        destination=destination.owner.username, amount=amount, \
                       currency=currency,motif=motif, who_approved=who_approved, \
                        )
        # responseOperation = 200
        if responseOperation == 200:
            invest_objet.code = responseCode
            invest_objet.date_deadline = datetime.now() + \
                  timedelta(days=(number*30))
            destination.save()
            source.save()
            invest_objet.save()
            return 200
        else:
            return 203
    else :
        return 204

    
def infoUser(user):
    """This is to return the gathered basic infos related to the user"""
    basic_info = {}
    try:
        basic_info['username'] = user.username
        basic_info['level'] = 1
    except AttributeError:
        pass
    try:
        basic_info['firstname'] = user.firstname
        basic_info['lastname'] = user.lastname
        basic_info['phonenumber'] = user.phonenumber
        basic_info['email'] = user.email
        basic_info['level'] = 2
    except AttributeError:
        pass 

    basic_info_serialized = BasicInfoSeria(basic_info)
    if basic_info_serialized.is_valid:
        print("Your Basic_info Serializer WORKED well")
        return basic_info_serialized.data #when things went well

    return 'infoUser' #when things didn't go well
 

class DepotOperations(viewsets.ViewSet):
    # company_solde = Solde.objects.get(pk=1)

    @action(methods=['post'], detail=False)
    def receiveDepot(self, request):
        dataSent = request.data
        bordereau = dataSent.get('bordereau')
        print("The things you sent are: ", request.data)
        print("The first element is : ", dir(dataSent))
        print("Now the first is : ", bordereau)
        newDepot = DepotPreuve.objects.create(bordereau=bordereau)
        newDepot.date_submitted = datetime.now()
        url = f"http://localhost:8002/jov/api/depot/{newDepot.id}/approveDepot/"
        newDepot.link_to_approve = url
        newDepot.currency = dataSent.get('currency')
        newDepot.montant = dataSent.get('montant')
        newDepot.deposant = dataSent.get('deposant')
        newDepot.numero = dataSent.get('numero')
        newDepot.owner = str(request.user)
        newDepot.save()
        return JsonResponse({"C'est": "bon"})
        pass

    @action(methods=['get'], detail=True)
    def approveDepot(self, request, pk):
        company_solde = Solde.objects.get(pk=2)
        depot = DepotPreuve.objects.get(pk=pk)
        depot.date_approved = timezone.now()
        depot.who_approved = str(request.user)
        # doing some operations
        owner_username = depot.owner
        owner = User.objects.get(username = owner_username)
        owner_id = owner.id
        currency = depot.currency
        actualSoldeObject = Solde.objects.get(owner_id=owner_id)
        #function that operates on Solde
        response = workOnSolde(company_solde, actualSoldeObject,\
                         depot.montant, currency, str(request.user.username))
        if response == 200:
            depot.approved = True
            depot.save()
            return JsonResponse({"C'est bien": "fait"})
        else:
            return JsonResponse({"C'est mal ": "passe"})
    
       
    

    @action(methods=['get'], detail=True)
    def getBordereau(self, request, pk):
        depot = DepotPreuve.objects.get(pk=pk)
        return JsonResponse({"The link :":\
                         f"http://127.0.0.1:8002{depot.get_bordereau_url()}"},\
                              safe=False)
    
    @action(methods=['get'], detail=False)
    def getDepotAll(self, request):
        depots = DepotPreuve.objects.all()[10::-1]
        depo_serializer = DepoSeria(depots, many=True)

        if depo_serializer.is_valid:
            return Response(depo_serializer.data)
        return Response(depo_serializer.data)
    
    @action(methods=['get'], detail=False)
    def getDepotNotDone(self, request):
        depots = DepotPreuve.objects.filter(approved=False)[::-1]
        depo_serializer = DepoSeria(depots, many=True)

        if depo_serializer.is_valid:
            return Response(depo_serializer.data)
        return Response(depo_serializer.data)@action(methods=['get'], detail=False)
    
    @action(methods=['get'], detail=False)
    def getDepotDone(self, request):
        depots = DepotPreuve.objects.filter(approved=True)[::-1]
        depo_serializer = DepoSeria(depots, many=True)

        if depo_serializer.is_valid:
            return Response(depo_serializer.data)
        return Response(depo_serializer.data)
    






class RetraitOperations(viewsets.ViewSet):
    @action(methods=['post'], detail=False,\
             permission_classes= [IsAuthenticated])
    def receiveRetrait(self, request):
        # parser_classes = [MultiPartParser]
        newRetrait = RetraitLives.objects.create(owner=request.user)
        dataSent = request.data
        newRetrait.owner = str(request.user.username)
        newRetrait.currency = dataSent.get('currency')
        newRetrait.numero = dataSent.get('numero')
        newRetrait.benefitor = dataSent.get('benefitor')
        newRetrait.montant = int(dataSent.get('montant'))
        newRetrait.date_submitted = timezone.now()
        url = f"http://localhost:8002/jov/api/retrait/{newRetrait.id}/approve/"
        newRetrait.link_to_approve = url
        newRetrait.save()
        return JsonResponse({"Things are ": "well"})
    
    @action(methods=['get'], detail=True,\
             permission_classes= [IsAuthenticated])
    def approve(self, request, pk):
        """We want to approve the WithDrawal"""
        retrait = RetraitLives.objects.get(pk=pk)
        company_solde = Solde.objects.get(pk=2)
        user = User.objects.get(username=str(retrait.owner))
        user_solde = Solde.objects.get(owner=user)

        # calling te function to handle the withdrawal
        reponse = workOnSolde(source=user_solde, destination=company_solde, \
                    amount=retrait.montant, currency=retrait.currency, \
                        who_approved=str(request.user), charge=1, \
                            motif='Retrait')
        
        if reponse == 200:
            retrait.approved = True
            retrait.save()

            # return Response
            return JsonResponse({"rapport": "ok"}, status=202)
        else:
            return JsonResponse({'rapport ': reponse}, status=201)
        return JsonResponse({"C'est ": "Bon"})

    
    @action(methods=['get'], detail=False,\
             permission_classes= [IsAuthenticated])
    def allRetraits(self, request):
        retraits = RetraitLives.objects.all()[::-1]
        retraits_serializer = RetraiSeria(retraits, many=True)

        if retraits_serializer.is_valid:
            # pass
            return Response(retraits_serializer.data)
        
        return JsonResponse({"The things are ": retraits_serializer.data})
    
    @action(methods=['get'], detail=False,\
             permission_classes= [IsAuthenticated])
    def needRetraits(self, request):
        retraits = RetraitLives.objects.filter(approved=False)[::-1]
        retraits_serializer = RetraiSeria(retraits, many=True)

        if retraits_serializer.is_valid:
            # pass
            return Response(retraits_serializer.data)
        
        return JsonResponse({"The things are ": retraits_serializer.data})
    
    @action(methods=['get'], detail=False,\
             permission_classes= [IsAuthenticated])
    def doneRetraits(self, request):
        retraits = RetraitLives.objects.filter(approved=True)[::-1]
        retraits_serializer = RetraiSeria(retraits, many=True)

        if retraits_serializer.is_valid:
            # pass
            return Response(retraits_serializer.data)
        
        return JsonResponse({"The things are ": retraits_serializer.data})
    



class InvestmentsOperations(viewsets.ViewSet):
    @action(methods=['post'], detail=False,\
             permission_classes= [IsAuthenticated])
    def receiveInvests(self, request):
        # parser_classes = [MultiPartParser]
        dataSent = request.data
        owner = User.objects.get(username=request.user)
        # owner = get_object_or_404(User, username=request.user)
        newInvestment = InvestmentsMade.objects.create()
        # newInvestment = InvestmentsMade()
        newInvestment.owner = owner.username
        # newInvestment.who_approved = owner
        newInvestment.currency = str(dataSent.get('currency'))
        newInvestment.capital = int(dataSent.get('capital'))
        newInvestment.taux = float(dataSent.get('taux'))
        newInvestment.duree = int(dataSent.get('duree'))
        newInvestment.interest = float((newInvestment.taux/100) * newInvestment.capital * (newInvestment.duree/12))
        newInvestment.result = newInvestment.capital + newInvestment.interest
        link = f"http://localhost:8002/jov/api/invest/{newInvestment.id}/approveInvest/"
        newInvestment.link_to_approve = link
        newInvestment.date_submitted = timezone.now()
        # newInvestment.owner = owner
        # print("THe owner is : ", type(owner))
        newInvestment.save()
        return JsonResponse({"Things are ": "well"})
    
    @action(methods=['get'], detail=True,\
             permission_classes= [IsAuthenticated])
    def approveInvest(self,request, pk):
        selected_investment = InvestmentsMade.objects.get(pk=pk)
        if not selected_investment.approved:
            # Calling a function that manages the Assignment
            investor = User.objects.get(username=selected_investment.owner)
            company_investment = User.objects.get(username='INVESTISSEMENT')
            solde_invester = Solde.objects.get(owner=investor)
            store_investment = Solde.objects.get(owner=company_investment)
            
            reponse = workOnSoldeInve(source=solde_invester, \
                            destination=store_investment, \
                            amount=selected_investment.capital, \
                            currency=selected_investment.currency, \
                            who_approved=str(request.user), \
                            number=selected_investment.duree,\
                            invest_objet=selected_investment, \
                            motif="Investissement",)
            
            selected_investment.approved = True
            selected_investment.who_approved = str(request.user)
            selected_investment.date_approved = timezone.now()
            # print("The sender is : ", request.user)
            selected_investment.save()
            return JsonResponse({"c'est ": f"{reponse}"})
        else:
            return JsonResponse({"This link is ": "used up"})
        return JsonResponse({"The things are well ": "terminated"})
    
    @action(methods=['get'], detail=False,\
             permission_classes= [IsAuthenticated])
    def allInvests(self, request):
        inve = InvestmentsMade.objects.all()
        inve_serializer = InveSeria(inve, many=True)

        if inve_serializer.is_valid:
            # pass
            return Response(inve_serializer.data)
        
        return JsonResponse({"The things are ": inve_serializer.data})
    
    @action(methods=['get'], detail=False,\
             permission_classes= [IsAuthenticated])
    def doneInvests(self, request):
        inve = InvestmentsMade.objects.filter(approved=True)
        inve_serializer = InveSeria(inve, many=True)

        if inve_serializer.is_valid:
            # pass
            return Response(inve_serializer.data)
        
        return Response(inve_serializer.data)
        # return JsonResponse({"The things are ": inve_serializer.data})
    

    @action(methods=['get'], detail=False,\
             permission_classes= [IsAuthenticated])
    def needInvests(self, request):
        inve = InvestmentsMade.objects.filter(approved=False)
        inve_serializer = InveSeria(inve, many=True)

        if inve_serializer.is_valid:
            # pass
            return Response(inve_serializer.data)
        
        return Response(inve_serializer.data)


class SoldeOperations(viewsets.ViewSet):

    @action(methods=['get'], detail=False,\
             permission_classes= [IsAuthenticated])
    def getSolde(self, request):
        owner_id = request.user.id
        solde_object = Solde.objects.get(owner_id=owner_id)
        print(f"The SOlde found is : {solde_object}")
        solde_serializer = SoldeSeria(solde_object)
        if solde_serializer.is_valid:
            return Response(solde_serializer.data)

        return JsonResponse({"Les choses sont: ": "bien passees"})


class Nofications(viewsets.ViewSet):
    """This is what is the response/message from the Backoffice"""

    @action(methods=['get'], detail=False,\
             permission_classes= [IsAuthenticated])
    def getAll(self, request):
        notifDepot = OperationStore.objects.filter(destination=str(request.user)).order_by('-date_approved')
        # notifDepot = InvestmentsMade.objects.filter(owner=str(request.user)).filter(approved=True).order_by('-date_approved')

        notifDepot_seria = OperationSeria(notifDepot, many=True)
        
        if notifDepot_seria.is_valid:
            return Response(notifDepot_seria.data)
        return Response(notifDepot_seria.data)
    
    @action(methods=['get'], detail=False,\
             permission_classes= [IsAuthenticated])
    def getHisto(self, request):
        notifDepot = OperationStore.objects.filter(source=str(request.user)).order_by('-date_approved')
        # notifDepot = InvestmentsMade.objects.filter(owner=str(request.user)).filter(approved=True).order_by('-date_approved')

        notifDepot_seria = OperationSeria(notifDepot, many=True)
        
        if notifDepot_seria.is_valid:
            return Response(notifDepot_seria.data)
        return JsonResponse({"rapport":'non'})
    
class SearchInfo(viewsets.ViewSet):
    @action(methods=['post'], detail=False,\
             permission_classes= [IsAuthenticated])
    def userAvailable(self, request):
        """Gives back: Info+Solde+Historique+Notifications related
        to the user"""
        dataReceived = request.data
        username = dataReceived.get('username')
        try:
            user_requested = User.objects.get(username=username)
        except User.DoesNotExist:
            return JsonResponse({"response":"new"}, status=200)
        else:
            soldeUser = Solde.objects.get(owner=user_requested)
            histoUser = OperationStore.objects.filter(source=user_requested.username)[::-1]
            notifs = OperationStore.objects.filter(destination=user_requested.username)[::-1]
            soldeUser_serializer = SoldeSeria(soldeUser)
            histoUser_serializer = OperationSeria(histoUser, many=True)
            notifs_serializer = OperationSeria(notifs, many=True)

            user_info = infoUser(user_requested)
            #printing something
            if (user_info is not str):
                print("THe things went really well")

            combined = []

            if ((soldeUser_serializer.is_valid and \
                histoUser_serializer.is_valid) and \
                (notifs_serializer.is_valid) and (user_info is not str)):
                combined = {
                    'info' : user_info,
                    'solde' : soldeUser_serializer.data,
                    'historique' : histoUser_serializer.data,
                    'notifications' : notifs_serializer.data,
                }
                # return JsonResponse({"response":"exist"}, status=200)
                return Response(combined)
            return JsonResponse({"response":"exist"}, status=200)
    
    @action(methods=['get'], detail=False,\
             permission_classes= [IsAuthenticated])
    def askCommissions(self, request):
        """Gives the actual commissions fees tables to be applied"""
        commission_actual = CommissionForWithdrawal.objects.last()
        commission_actual_serializer = CommissionSeria(commission_actual)

        if commission_actual_serializer.is_valid:
            return Response(commission_actual_serializer.data)
        return JsonResponse({"rapport":'non'})
    
    @action(methods=['post'], detail=False)
    def usernameExist(self, request):
        sent_data = request.data
        print(f"The sent username is : {sent_data}")
        return JsonResponse({"rapport": 1}, status=201)

    @action(methods=['post'], detail=False)
    def emailExist(self, request):
        sent_data = request.data
        print(f"The sent email is : {sent_data}")
        return JsonResponse({"rapport": 1}, status=200)



# class FatherUser(viewsets.ViewSet):
#     """This is for giving birth of the new user, updating"""
#     @action(methods=['post'], detail=False,\
#              permission_classes= [IsAuthenticated])
#     def addUser(self, request):
#         data_sent =request.data

class FatherUser(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSeriazer

    @action(methods=['post'], detail=False,)
    def poolUser(self, request):
        sent_data =request.data
        # data = {key: value for key, value in request.data.items()}
        # print(f"The sent username is : {sent_data}")
        code = GenerateCode(high=6)
        code_pool = code.gene()
        data = ['','']
        data[0] = sent_data
        data[1] = code_pool
        saved_pool = self._addPool(data=data)
        pool_user_serializer = PoolUserSeria(saved_pool)
        if pool_user_serializer.is_valid:
            print(f"The collected data is : {(saved_pool.__dict__)}")
        return JsonResponse({"rapport": 1}, status=201)
    
    def is_valid_email(self, email):
        try:
            validate_email(email)
            return True
        except ValidationError:
            return False
        
    def is_gt_seven(self, pwd):
        if len(pwd) > 7:
            return True
        else :
            return False
        
    def _addPool(self, data):
        """Creates a new PoolUser instance and populates it"""
        new_pool = PoolUser.objects.create()

        new_pool.code = data[1]

        username = self.is_gt_seven(data[0].get('username'))
        if username:
            new_pool.username = data[0].get('username')

        password = self.is_gt_seven(data[0].get('password'))
        if password:
            new_pool.password = data[0].get('password')

        email = self.is_valid_email(data[0].get('email'))
        if email:
            new_pool.email = data[0].get('email')

        phone = self.is_gt_seven(data[0].get('phone'))
        if phone:
            new_pool.phone = data[0].get('phone')

        new_pool.date_submitted = timezone.now()

        return new_pool

