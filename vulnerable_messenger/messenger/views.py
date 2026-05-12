from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User


def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        user_id = request.POST.get('user_id')
        #this shouldn't be here
        isadmin = request.POST.get('isadmin') == 'on'

        if name and user_id:
            User.objects.create(name=name, user_id=int(user_id), isadmin=isadmin)
            return redirect('index')
    
    users = User.objects.all()
    return render(request, 'messenger/index.html', {'users': users})

def messages(request, user_id):
    return HttpResponse("Here be the messages that you should see")


