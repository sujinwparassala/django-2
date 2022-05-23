from django.shortcuts import render
from . import forms
from fifthApp.models import computer_list

# Create your views here.

#def home(request):
    #return render(request,'fifthApp/index.html')


def education(request):
    
    return render(request,'fifthApp/index.html')


def contact(request):

    contact_form = forms.computer_stoke()
    computer_info = {'education_form':contact_form}
    return render(request,'fifthApp/contact.html',context=computer_info)

def project(request):
    return render(request,'fifthApp/project.html')

def photos(request):
    return render(request,'fifthApp/photos.html')

def resume(request):
    return render(request,'fifthApp/resume.html')

def certificate(request):
    return render(request,'fifthApp/certificate.html')

"""def cookies(request):
    count = request.COOKIES.get('count',0)
    total_count = int(count)+1
    response = render(request,'fifthApp/cookiescount.html',{'count':total_count})
    response.set_cookie('count',total_count)
    return response"""
def cookies(request):
    count = request.session.get('count',0)
    total_count = int(count+1)
    request.session['count'] = total_count
    print(request.session.get_expiry_date())
    return render(request,'fifthApp/cookiescount.html',{'count':total_count})



def retrive(request):
    student = computer_list.objects.all()
    return render(request,'fifthApp/cookiescount.htm',{'student':student})

