from django.shortcuts import render
from django.http import JsonResponse
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Person
from .serializers import PersonSeriazer

# Create your views here.


class ShowPerson:
    all_persons = Person.objects.all()

    def get(self, request):
        data = {"a": 1}
        return JsonResponse(data=data)
        # names = {}
        # names = {x['name'] =  for x in self.all_person}
        # return {"a":"ab"}

def show_person(request):
    last_personne = Person.objects.first()
    personne_serialized = model_to_dict(last_personne, \
                                        fields=['name', 'message', 'id'])

    # print(names_liste)
    data = {"a": 1}
    return JsonResponse(personne_serialized)

@api_view (['GET','POST'])
def apiRoot(request):
    """Returning all the objects"""
    data = Person.objects.all()
    data_serialized = PersonSeriazer(data, many=True)
    print(f"The data is: {data_serialized}")
    # return JsonResponse(data_serialized, safe=False)
    return Response(data_serialized.data, 200)