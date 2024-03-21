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
    date = models.DateTimeField(default=datetime.now())

    def __str__(self) -> str:
        return str(f"Depot ({self.currency}), {self.montant}")
    
    def get_bordereau_url(self):
        if self.bordereau:
            return self.bordereau.url
        else:
            return ''


class RetraitLives(models.Model):
    currency = models.CharField(max_length=10, default="null")
    numero = models.CharField(max_length=25, default="numerovide")
    benefitor = models.CharField(max_length=25, default="nulldeposant")
    montant = models.IntegerField(help_text="Le montant que vous deposez",\
                                  default=0)
    date_submitted = models.DateTimeField(default=timezone.now())
    date_approved = models.DateTimeField(default=timezone.now())
    # who_approved = models.ForeignKeymodels.ForeignKey(User, on_delete=models.CASCADE)
    # owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(f"Retrait ({self.currency}), {self.montant}")