from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def contact(request):
    if request.method == 'POST':
        # Получение данных из формы
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(name, email, message)
        request.status_post = True
    else:
        request.status_post = False
    return render(request, 'contact.html')

