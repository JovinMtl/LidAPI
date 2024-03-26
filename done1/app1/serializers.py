from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Person, Requeste, PorteFeuille

from .models import InvestmentsMade, DepotPreuve, Solde, OperationStore



class PersonSeriazer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ['name','id']

class UserSeriazer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    
class RequeSeria(serializers.ModelSerializer):
    class Meta:
        model = Requeste
        fields = '__all__'

class PorteSeria(serializers.ModelSerializer):
    class Meta:
        model = PorteFeuille
        fields = '__all__'

class InveSeria(serializers.ModelSerializer):
    class Meta:
        model = InvestmentsMade
        fields = '__all__'

class DepoSeria(serializers.ModelSerializer):
    class Meta:
        model = DepotPreuve
        fields = '__all__'

class SoldeSeria(serializers.ModelSerializer):
    class Meta:
        model = Solde
        fields = '__all__'

class OperationSeria(serializers.ModelSerializer):
    class Meta:
        model = OperationStore
        fields = '__all__'