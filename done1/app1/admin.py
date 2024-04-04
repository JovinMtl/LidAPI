from django.contrib import admin

from .models import Person, Requeste, PorteFeuille, Recharge, Differente,\
                    Trade, DepotPreuve, RetraitLives, InvestmentsMade,\
                          Solde, OperationStore, CommissionForWithdrawal, \
                          InterestRateForInvestment


# Changing the Panel name
new_name = "'Lit Dinar' All Power Panel  ---  (iyi ni Danger zone)"
admin.site.site_header = new_name


#making the readonly fields to appeal in django admin site

class OperationStoreAdmin(admin.ModelAdmin):
    readonly_fields = ('code',)

class DepotPreuveAdmin(admin.ModelAdmin):
    readonly_fields = ('link_to_approve',)

class Retraits(admin.ModelAdmin):
    readonly_fields = ('link_to_approve','owner',)

class SoldeAdmin(admin.ModelAdmin):
    readonly_fields = ('owner',)


# Register your models here.

# admin.site.register(Person)
# admin.site.register(Requeste)
# admin.site.register(PorteFeuille)
# admin.site.register(Recharge)
# admin.site.register(Differente)
# admin.site.register(Trade)
admin.site.register(DepotPreuve, DepotPreuveAdmin)
admin.site.register(RetraitLives, Retraits)
admin.site.register(InvestmentsMade)
admin.site.register(InterestRateForInvestment)
# admin.site.register(Solde, SoldeAdmin)
admin.site.register(Solde)
admin.site.register(OperationStore, OperationStoreAdmin)
admin.site.register(CommissionForWithdrawal)