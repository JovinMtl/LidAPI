from django.contrib import admin

from .models import Person, Requeste, PorteFeuille, Recharge, Differente,\
                    Trade, DepotPreuve, RetraitLives


# Changing the Panel name
new_name = "'Lit Dinar' All Power Panel  ---  (iyi ni Danger zone)"
admin.site.site_header = new_name


# Register your models here.

admin.site.register(Person)
admin.site.register(Requeste)
admin.site.register(PorteFeuille)
admin.site.register(Recharge)
admin.site.register(Differente)
admin.site.register(Trade)
admin.site.register(DepotPreuve)
admin.site.register(RetraitLives)