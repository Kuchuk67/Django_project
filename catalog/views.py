from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def contact(request):
    #print({{ request.path }})
    return render(request, 'contact.html')

