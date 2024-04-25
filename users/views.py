from django.contrib import auth
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse

from users.forms import UserLoginForm

# Create your views here.

def login(request):
    
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            
            user = auth.authenticate(username=username, password=password)
            
            if user:
                auth.login(request, user)
                
                return redirect('') # add where to redirect
            
    else:
        form = UserLoginForm()
        
    
    context = {
        'title' : 'Login page',
        'form' : form
    }
    return render(request, 'users/login.html', context=context)
