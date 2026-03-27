from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Home(request):
    return render(request, 'home.html')

def Education(request):
    return render(request ,'education.html')

def Projects(request):
    return render(request , 'projects.html')

def Extras(request):
    return render(request, 'extras.html')

def travel(request):
    return render(request, 'travel.html')

from .models import Contact

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        Contact.objects.create(
            name=name,
            email=email,
            phone=phone,
            message=message
        )

    return render(request, 'contact.html')


def Certificates(request):
    return render(request, 'certificate.html')