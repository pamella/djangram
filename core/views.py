from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'text': 'Hello world',
        'name': 'pam',
    }
    return render(request, 'index.html', context)