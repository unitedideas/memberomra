from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'members/home.html')

def search(request):
    return render(request, 'members/search.html')

def add(request):
    return render(request, 'members/add.html')


