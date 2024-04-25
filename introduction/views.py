from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title' : 'Introduction page',
    }
    return render(request, 'introduction/index.html', context)
