from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    context_dict = {'boldmessage': 'Crunchy, creamy, candy, cupcake!'}
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    context_dict = {'boldmessage': 'this project was made by Kai Hasse'}
    return render(request, 'rango/about.html', context=context_dict)
