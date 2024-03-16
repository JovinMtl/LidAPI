from django.contrib import admin

from .models import Person, Requeste, PorteFeuille, Recharge, Differente,\
                    Trade

# Register your models here.

admin.site.register(Person)
admin.site.register(Requeste)
admin.site.register(PorteFeuille)
admin.site.register(Recharge)
admin.site.register(Differente)
admin.site.register(Trade)