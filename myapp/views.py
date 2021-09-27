from django.shortcuts import render
from .models import Contact

# Create your views here.


def home(request):
    name = ['Rifat', 'Tahsin', 'Asif', 'Arman']
    contex = {
        'name':name
    }
    return render(request, 'index.html', contex)


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        text = request.POST['text']
        obj = Contact(name = name, email = email, text = text)
        obj.save()

    return render(request, 'contact.html')
