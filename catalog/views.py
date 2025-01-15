from django.shortcuts import render
from .models import  PageBlock
from catalog.src.new_products import new_product

# Create your views here.

def home(request):
    data =new_product()
    return render(request, 'home.html', context=data)

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

    data_c = {"contacts_title": '', "contacts_txt": ''}
    for x in b_tests:
        data_c = {"contacts_title": x.title, "contacts_txt": x.text}

    return render(request, 'contacts.html', context=data_c)

