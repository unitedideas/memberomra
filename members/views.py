from django.core.serializers import serialize
from django.db.models import Q
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from members.forms import AddMemberForm
from .models import *
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
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
    if request.method == 'POST':
        add_member_form = AddMemberForm(request.POST)
        if add_member_form.is_valid():
            add_member_form.save()
            return HttpResponseRedirect('/add')
        else:
            args = {'form': add_member_form, 'errors': add_member_form.errors}
            return render(request, 'members/add.html', args)
    else:
        add_member_form = AddMemberForm()
        return render(request, 'members/add.html', {'form': add_member_form})


def member_search(request):
    search_data = json.load(request)
    search_results = ""

    if request is not None:
        search_results = Rider.objects.filter(Q(firstName__isnull=True) | Q(firstName__contains=search_data["firstName"]))
        search_results = search_results.filter(Q(lastName__isnull=True) | Q(lastName__contains=search_data["lastName"]))
        search_results = search_results.filter(Q(email__isnull=True) | Q(email__contains=search_data["email"]))
        search_results = search_results.filter(Q(memberNumber__isnull=True) | Q(memberNumber__contains=search_data["memberNumber"])).order_by('lastName')
        # search_results = Rider.objects.all()
        search_results = serialize('json', search_results)

    return JsonResponse({"search_results": search_results})


def edit_member(request):
    """ Allows an admin to edit member data """
    if request.method == 'POST':
        edit_form = AddMemberForm(request.POST)
        if edit_form.is_valid():
            for data in edit_form:
                print(data)
                return HttpResponseRedirect('/search')
        else:
            args = {'edit_form': edit_form, 'errors': edit_form.errors}
            return render(request, 'members/add.html', args)
    else:
        edit_form = AddMemberForm()
        return render(request, 'members/add.html', {'edit_form': edit_form})


def delete_member(request):
    pass
