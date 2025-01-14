from django.shortcuts import render
from .models import  PageBlock

# Create your views here.

def home(request):
    return render(request, 'home.html')

def contacts(request):
    if request.method == 'POST':
        # Получение данных из формы
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(name, email, message)
        request.status_post = True
    else:
        request.status_post = False
    b_tests = PageBlock.objects.filter(id=1)
    for x in b_tests:
        data = {"contacts_title": x.title, "contacts_txt": x.text}
    return render(request, 'contacts.html', context=data)

