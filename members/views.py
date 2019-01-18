from django.core.serializers import serialize
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from members.forms import AddMemberForm
from .models import *
from django.http import JsonResponse, HttpResponseRedirect
import json


def home(request):
    """
    Using the LoginView.auth
    If the user is not logged and tries to access any other page they will be directed to this page.
    If they are authenticated they will default to the search page.
    """
    pass


@login_required(login_url='')
def search(request):
    """ Allows for the async search of members in the database """
    return render(request, 'members/search.html')


@login_required(login_url='')
def add(request):
    """ Allows an admin to manually add members to the database """
    print(request.method)
    if request.method == 'POST':
        print('post method')
        form = AddMemberForm(request.POST)
        if form.is_valid():
            print('success')
            form.save()
            return HttpResponseRedirect('/add')
        else:
            print('error')
            render(request, 'members/add.html', {'form': form})
    else:
        print('get method')
        form = AddMemberForm()
        return render(request, 'members/add.html', {'form': form})


def member_search(request):
    search_data = json.load(request)
    search_results = ""

    if request is not None:
        search_results = Rider.objects.filter(firstName__contains=search_data["firstName"])
        search_results = search_results.filter(lastName__contains=search_data["lastName"])
        search_results = search_results.filter(memberNumber__contains=search_data["memberNumber"])
        search_results = serialize('json', search_results)

    return JsonResponse({"search_results": search_results})
