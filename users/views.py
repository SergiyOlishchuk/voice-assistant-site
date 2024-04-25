from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def login(request):
    context = {
        'title' : 'Login page',
    }
    return render(request, 'users/login.html', context=context)