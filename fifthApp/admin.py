from django.contrib import admin
from fifthApp.models import computer_list


# Register your models here.

class computer_listAdmin(admin.ModelAdmin):
    list = ['slno','amount','section','order']
   #admin.site.register(computer_list,computer_listAdmin)
    admin.site.register(computer_list)