from django.shortcuts import render
from django.contrib.auth.decorators import login_required


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
