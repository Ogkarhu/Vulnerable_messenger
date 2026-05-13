from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User


def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        isadmin = request.POST.get('isadmin') == 'on'

        if name:
            User.objects.create(name=name, isadmin=isadmin)
            return redirect('index')
    
    users = User.objects.all()
    return render(request, 'messenger/index.html', {'users': users})

def messages(request, user_id):
    return HttpResponse("Here be the messages that you should see")

def login(request):
    
    return render(request, 'messenger/login.html')

def register(request):
    pass




