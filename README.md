# Ex02 Django ORM Web Application
## Date: 4/11/2024

## AIM
To develop a Django application to store and retrieve data from a Book database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM

![WhatsApp Image 2024-11-16 at 13 31 20_97756311](https://github.com/user-attachments/assets/d5e2a857-d66a-47c9-8622-ea81a6676b4e)

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 customers.

## PROGRAM
~~~
Admin.py

from django.contrib import admin
from .models import Bank_loan,Bank_loanAdmin
admin.site.register(Bank_loan,Bank_loanAdmin)
~~~
~~~
Models.py

from django.db import models
from django.contrib import admin
class Bank_loan (models.Model):
    customer_id=models.IntegerField(primary_key=True)
    customer_name=models.CharField(max_length=100)
    loan_amount=models.IntegerField()
    customer_age=models.IntegerField()
    email=models.EmailField()

class Bank_loanAdmin(admin.ModelAdmin):
    list_display=('customer_id','customer_name','loan_amount','customer_age','email')
~~~

## OUTPUT

![Screenshot 2024-11-16 141425](https://github.com/user-attachments/assets/de245d2b-cd78-4917-93ac-a5f6544f43a7)

## RESULT
Thus the program for creating a database using ORM hass been executed successfully
