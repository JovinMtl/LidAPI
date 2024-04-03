from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import User


"""This is for my models"""

class Person(models.Model):
    
    name = models.CharField(max_length=15)
    account = models.IntegerField(default=0)

    @property
    def message(self):
        return f"Hello {self.name}"
    
    def __str__(self) -> str:
        return f"{self.name}, {self.id}"

states = ((1, 'Pending'), (2, 'Done'))
payments = [(1, 'LUMICASH'),(2, 'PAYPAL'),(3, 'eNOTI')]



class Requeste(models.Model):
    """Same as operations Table"""
    amount_to_send = models.IntegerField(default=0)
    receiver_number = models.IntegerField(default=0)
    amount_to_deb = models.IntegerField(default=0)
    state_progress = models.IntegerField(choices=states,\
                                          default=states[0][0])
    pay_method = models.IntegerField(choices=payments, default=1)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    user_username = models.CharField(max_length=15)
    date_created = models.DateTimeField(default=datetime.now())
    date_approved = models.DateTimeField(default=datetime.now())
    link_to_activate = models.URLField(\
        default='http://127.0.0.1:8000/jov/api/users//')
    approved_by = models.CharField(max_length=15, default="None")

    def __str__(self):
        return f"{str(self.amount_to_deb)}, {str(self.id)}"



class Recharge(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.IntegerField(default=0)
    amount = models.IntegerField(default=0)
    code_transaction = models.CharField(max_length=15 ,default='xdf')
    date_action = models.DateTimeField(default=datetime.now())

class Differente(models.Model):
    name = models.CharField('Vente ou Achat', max_length=10, \
                            default="Vente")
    date = models.DateField(default=datetime.now())
    lumicash = models.IntegerField(default=0)
    lid = models.IntegerField(default=0)
    mpesa = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.date} : {self.lumicash} : {self.name}"

class Trade(models.Model):
    buy = models.ForeignKey(Differente, on_delete=models.CASCADE,\
                            related_name="we_want_to_buy_the_lid")
    sell = models.ForeignKey(Differente, on_delete=models.CASCADE,\
                             related_name="we_want_to_sell_the_Lid")
    date = models.DateField(default=datetime.now())
    
    def __str__(self) -> str:
        return f"Trade of {self.date}"

class PorteFeuille(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    owner_username = models.CharField('to be deprecated',\
                                      max_length=15, default="Noe")
    lumicash = models.IntegerField(default=0)
    lid = models.FloatField(default=0.0)
    mpesa = models.IntegerField(default=0)

    def __str__(self) -> str:
        return str(f"{self.owner_username} , {self.lumicash}, \
                   {self.lid}")

class DepotPreuve(models.Model):
    currency = models.CharField(max_length=10, default="null")
    deposant = models.CharField(max_length=25, default="nulldeposant")
    numero = models.CharField(max_length=25, default="numerovide")
    montant = models.IntegerField(help_text="Le montant que vous deposez",\
                                  default=0)
    bordereau = models.ImageField(upload_to='depots/')
    # owner = models.ForeignKey(User, on_delete=models.CASCADE)

    owner = models.CharField(max_length=10, default="null")
    who_approved = models.CharField(max_length=10, default="null")
    date_submitted = models.DateTimeField(default=datetime.now())
    link_to_approve = models.URLField(max_length=50, \
                default="http://localhost:8002/jov/api/depot/4/approveDepot/",\
                editable=False)
    date_approved = models.DateTimeField(default=datetime.now())
    approved = models.BooleanField(default=False)

    def __str__(self) -> str:
        return str(f"Depot {self.id} ({self.approved}) , {self.montant}({self.currency}), \
                   {self.deposant}, {str(self.date_submitted)[:16]}.")
    
    def get_bordereau_url(self):
        if self.bordereau:
            return self.bordereau.url
        else:
            return ''


class RetraitLives(models.Model):
    currency = models.CharField(max_length=10, default="null")
    numero = models.CharField(max_length=25, default="numerovide")
    benefitor = models.CharField(max_length=25, default="nulldeposant")
    montant = models.IntegerField(help_text="Le montant que vous Retirer",\
                                  default=0)
    date_submitted = models.DateTimeField(default=timezone.now())
    date_approved = models.DateTimeField(default=timezone.now())
    # owner = models.ForeignKey(User, on_delete=models.CASCADE, \
    #                           related_name="The_one_who_initiated")
    owner = models.CharField(max_length=10, default="null")
    who_approved = models.CharField(max_length=10, default="null")
    link_to_approve = models.URLField(max_length=50, \
                default="http://localhost:8002/jov/api/depot/4/approveDepot/",\
                editable=False)
    approved = models.BooleanField(default=False)

    def __str__(self) -> str:
        return str(f"Retrait  {self.montant}({self.currency}), \
                   {self.benefitor}, {str(self.date_submitted)[:16]}.")


class InvestmentsMade(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    currency = models.CharField(max_length=10, default="null")
    capital = models.IntegerField(help_text="Le montant que vous voulez \
                                  investir", default=0)
    taux = models.FloatField(help_text="Le taux d'interet annuel",\
                              default=0)
    duree = models.IntegerField(help_text="Le duree que vous devez \
                                  attendre", default=0)
    interest = models.IntegerField(help_text="votre benefice", default=0)
    result = models.IntegerField(help_text="Le montant que vous aurez \
                                  investir", default=0)
    # interest = (taux / 100) * capital.value * (duree/12) //simple
    date_submitted = models.DateTimeField(default=datetime.now())
    date_approved = models.DateTimeField(default=datetime.now())
    # owner = models.ForeignKey(User, on_delete=models.CASCADE, \
    #                           related_name="The_one_who_initiated")
    owner = models.CharField(max_length=10, default="null")
    who_approved = models.CharField(max_length=10, default="null")
    # who_approved = models.ForeignKey(User, on_delete=models.CASCADE, \
    #                           related_name="The_one_who_authorized_this")
    link_to_approve = models.URLField(max_length=50, \
                                        default='http://127.0.0.1:8002/jov/api/',\
                                        editable=False)
    approved = models.BooleanField(default=False)


    def __str__(self) -> str:
        return str(f"Invest({self.approved})  {self.capital}({self.currency}), \
                   {self.duree}mois,{self.interest},\
                      {str(self.date_submitted)[:16]}.")

class Solde(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    # owner = models.ForeignKey(User, on_delete=models.CASCADE)
    usdt = models.FloatField(help_text="Le solde actuel en usdt",\
                              default=0)
    usd = models.FloatField(help_text="Le solde actuel en US Dollar",\
                              default=0)
    bif = models.FloatField(help_text="Le solde actuel en FBU",\
                              default=0)
    rwf = models.FloatField(help_text="Le solde actuel en Frw",\
                              default=0)
    kes = models.FloatField(help_text="Le solde actuel en ShillingKenya",\
                              default=0)
    ugx = models.FloatField(help_text="Le solde actuel en Ugshilling",\
                              default=0)
    tsh = models.FloatField(help_text="Le solde actuel en ShillingTanzania",\
                              default=0)
    zmw = models.FloatField(help_text="Le solde actuel en Kwacha",\
                              default=0)
    eur = models.FloatField(help_text="Le solde actuel en Euro",\
                              default=0)
    trx = models.FloatField(help_text="Le solde actuel en TRX",\
                              default=0)
    lid = models.FloatField(help_text="Le solde actuel en Lit Dinar",\
                              default=0)
    
    def __str__(self) -> str:
        return f"Solde de {self.owner.username} en USDT: {self.usdt}."


class OperationStore(models.Model):
    code = models.CharField(max_length=15, unique=True, editable=False)
    source = models.CharField(max_length=15)
    destination = models.CharField(max_length=15, default="null")
    amount = models.IntegerField(help_text="Le montant de l'operation",\
                                  default=0)
    currency = models.CharField(max_length=10, default="null")
    motif = models.CharField(max_length=25)
    charge = models.IntegerField(help_text="La charge de l'operation",\
                                  default=0)
    date_approved = models.DateTimeField(default=datetime.now())
    who_approved = models.CharField(max_length=15, default="null")

    def __str__(self) -> str:
        return f"{self.motif}: {self.amount}({self.currency}); {(str(self.date_approved))[:16]};\
              #{self.code} ."


class CommissionForWithdrawal(models.Model):
    """THis one will store the fees we charge for withdrawal 
    on each currency. for example: 1/1000(1$ on up to 1000$)"""
    bif = models.CharField(max_length=30, default="5_000/1_000_000")
    eur = models.CharField(max_length=15, default="1/1_000")
    kes = models.CharField(max_length=20, default="50/1_000")
    rwf = models.CharField(max_length=25, default="3_000/1_000_000")
    trx = models.CharField(max_length=15, default="1/1_000")
    tsh = models.CharField(max_length=30, default="5_000/1_000_000")
    ugx = models.CharField(max_length=30, default="8_000/1_000_000")
    usd = models.CharField(max_length=15, default="1/1_000")
    usdt = models.CharField(max_length=15, default="1/1_000")
    zmw = models.CharField(max_length=30, default="5_000/1_000_000")
    date_approved = models.DateTimeField(default=datetime.now())
    who_approved = models.CharField(max_length=15, default="null")

    def __str__(self) -> str:
        return f"Commission on {(str(self.date_approved))[:11]}"