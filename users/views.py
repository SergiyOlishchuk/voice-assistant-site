from django.contrib import auth
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from users.forms import UserLoginForm, UserRegistrationForm

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
                
                redirect_page = request.POST.get('next', None)
                if redirect_page and redirect_page != reverse('user:logout'):
                    return redirect(redirect_page)
                
                return redirect(reverse('introduction:index'))
            
    else:
        form = UserLoginForm()
        
    
    context = {
        'title' : 'Login page',
        'form' : form
    }
    return render(request, 'users/login.html', context=context)

def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        
        if form.is_valid():
            form.save()
            
            user = form.instance
            auth.login(request, user)
            
            return redirect(reverse('introduction:index'))
        
    else:
        form = UserRegistrationForm()
        
    context = {
        'title' : 'Registration page',
        'form' : form,
    }
    
    return render(request, 'users/registration.html', context)

@login_required
def logout(request):
    auth.logout(request)
    return redirect(reverse('introduction:index'))
