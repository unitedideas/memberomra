""" Turn these off when running on server"""

import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "memberomra.settings")
django.setup()

"""connect to the squarespace api
    authinticate

retrieve the json (GET /commerce/orders/<id>/fulfillments=PENDING)

store the data in the correct fields

Depending on how omra takes orders (digital goods?)

(POST /commerce/orders/<id>/fulfillments)
Header:
api key
json application
body:
{ "shouldSendNotification":"false" }
"""
from django.core.management.base import BaseCommand
import json
import requests
from memberomra.secrets import OMRA_API_KEY
from members.models import Rider


def add_members():
    """connect to squarespace API"""

    baseUrl = 'https://api.squarespace.com/1.0/commerce/orders'

    headers = {
        'Authorization': OMRA_API_KEY,
    }

    params = (
        ('fulfillmentStatus', 'PENDING'),
    )

    # First Name
    # Last Name
    # Current Rider OMRA Number
    # Rider Age *
    # Rider Birth Date *
    # MC Brand and Model
    # Email Address *
    # Class *

    response = requests.get(baseUrl, headers=headers, params=params)
    pendingMembers = response.json()
    # customizations
    custom_form_data = pendingMembers['result']
    for each in custom_form_data:
        for rider in each['lineItems']:
            key_list = []
            data_list = []
            member_id = each['id']
            print(member_id)
            try:
                for eachItem in rider['customizations']:
                    for value in eachItem:
                        if value == 'label':
                            key_list.append(eachItem[value])
                        if value == 'value':
                            data_list.append(eachItem[value])
                doc_zip = dict(zip(key_list, data_list))
                if (len(doc_zip)) < 7:
                    print('-----------------------------------')
                    doc_zip['Class'] = "None"
                    print(len(doc_zip))
                r = json.dumps(doc_zip)
                print(r)

                headers = {
                    'Authorization': OMRA_API_KEY,
                    'content-type': 'application/json',
                }

                body = {
                    "shouldSendNotification": 'false',
                }

                # fulfill = requests.post(
                #     'https://api.squarespace.com/1.0/commerce/orders/' + member_id + '/fulfillments', headers=headers,
                #     json=body)
                # print(fulfill)

                # Get or create rider object
                # post rider fulfilled and shouldSendNotification":"false"

                # Rider.objects.get_or_create(
                #     firstName='John',
                #     lastName='Smith',
                # )

            except TypeError:
                print('TypeError')

    # firstName
    # lastName
    # phoneNumber
    # email
    # birthDate
    # memberNumber
    # plateNumber
    # membershipYear
    # motorcycleBrandAndModel
    # riderClass


add_members()


class Command(BaseCommand):
    def handle(self, *args, **options):
        add_members()
