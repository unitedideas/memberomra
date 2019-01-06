from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, 'members/home.html')


@login_required(login_url='')
def search(request):
    return render(request, 'members/search.html')


@login_required(login_url='')
def add(request):
    return render(request, 'members/add.html')
