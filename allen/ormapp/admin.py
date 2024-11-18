from django.contrib import admin
from . models import Bank_loan, Bank_loanAdmin

admin.site.register(Bank_loan,Bank_loanAdmin)