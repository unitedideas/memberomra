from django.core.serializers import serialize
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from members.forms import MemberForm
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
        add_member_form = MemberForm(request.POST)
        if add_member_form.is_valid():
            add_member_form.save()
            return HttpResponseRedirect('/add')
        else:
            args = {'form': add_member_form, 'errors': add_member_form.errors}
            return render(request, 'members/add.html', args)
    else:
        add_member_form = MemberForm()
        print(add_member_form)
        return render(request, 'members/add.html', {'form': add_member_form})


def member_search(request):
    search_data = json.load(request)
    search_results = ""

    if request is not None:
        search_results = Rider.objects.filter(
            Q(firstName__isnull=True) | Q(firstName__contains=search_data["firstName"]))
        search_results = search_results.filter(Q(lastName__isnull=True) | Q(lastName__contains=search_data["lastName"]))
        search_results = search_results.filter(Q(email__isnull=True) | Q(email__contains=search_data["email"]))
        search_results = search_results.filter(
            Q(memberNumber__isnull=True) | Q(memberNumber__contains=search_data["memberNumber"])).order_by('lastName')

        search_results = serialize('json', search_results)

    return JsonResponse({"search_results": search_results})


@login_required(login_url='')
def edit_member(request):
    """ Allows an admin to manually add members to the database """
    if request.method == 'POST':
        pk = request.GET.get('pk')
        member_to_edit = get_object_or_404(Rider, id=pk)
        edit_member_form = MemberForm(request.POST or None, instance=member_to_edit)
        if edit_member_form.is_valid():
            edit_member_form.save()
            return HttpResponseRedirect('/search', {'success': True})
        else:
            args = {'form': edit_member_form, 'errors': edit_member_form.errors}
            return render(request, 'members/edit_member.html', args)
    else:
        pk = request.META['HTTP_PK']
        edit_form = get_object_or_404(Rider, id=pk)
        edit_form = MemberForm(instance=edit_form)
        args = {'form': edit_form, 'pk': pk}
        return render(request, 'members/edit_member.html', args)


def delete_member(request):
    pass
