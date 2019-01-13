from django.core.serializers import serialize
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *
from django.http import JsonResponse
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
    return render(request, 'members/add.html')


def member_search(request):
    search_data = json.load(request)
    print(search_data)
    first_name_result = ""
    print("-------------------------------------------------------------")
    print(search_data["firstName"])
    print("-------------------------------------------------------------")

    if request is not None:
        first_name_result = serialize('json', Rider.objects.filter(firstName__contains=search_data["firstName"]))
        # first_name_result = {"results": [
        #     {'id': 1, 'firstName': 'Shane', 'lastName': 'Cheek', 'memberNumber': '123', 'plateNumber': '123A',
        #      'expirationDate': datetime.date(2019, 12, 31), 'active': True},
        #     {'id': 2, 'firstName': 'Other', 'lastName': 'Rider', 'memberNumber': '456', 'plateNumber': '456A',
        #      'expirationDate': datetime.date(2019, 12, 31), 'active': True}]}
        print(first_name_result)

    return JsonResponse({"results": first_name_result})
