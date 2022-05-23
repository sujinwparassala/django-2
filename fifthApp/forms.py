from django  import forms
from .models import computer_list
from . import views

# Register your forms here.


class computer_stoke(forms.Form):
    slno = forms.IntegerField()
    amount = forms.IntegerField()
    section = forms.CharField(max_length=10)
    order = forms.CharField(max_length=10)
