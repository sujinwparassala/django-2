from django.db import models
from fifthApp import forms
from fifthApp.models import computer_list

# Create your models here.

"""class computer_list(models.Model):
    slno = models.CharField(max_length=50)
    section = models.CharField(max_length=10)
    order = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)"""


class Meta:
    model = computer_list
    fields = '__all__'



class computer_listForm(forms.ModelForm):
    slno = models.CharField(max_length=50)
    section = models.CharField(max_length=10)
    order = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
