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
{ "shouldSendNotification":"true" }
"""
import sys
import json
import requests
from memberomra.secrets import OMRA_API_KEY

"""connect to squarespace API"""

baseUrl = 'https://api.squarespace.com/1.0/commerce/orders'

# curl "https://api.squarespace.com/1.0/commerce/orders?modifiedAfter=2016-04-10T12:00:00Z&modifiedBefore=2016-04-15T12:30:00Z" -H "Authorization: Bearer df7d9174-295d-4730-b73d-4f97230c1838"
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


# how to update the dict
# my_dict.update({'corse': 'my new definition'})


response = requests.get('https://api.squarespace.com/1.0/commerce/orders/', headers=headers, params=params)
pendingMembers = response.json()
# customizations
custom_form_data = pendingMembers['result']
for each in custom_form_data:
    for rider in each['lineItems']:
        key_list = []
        data_list = []
        try:
            for eachItem in rider['customizations']:
                for value in eachItem:
                    if value == 'label':
                        key_list.append(eachItem[value])
                    if value == 'value':
                        data_list.append(eachItem[value])
            doc_zip = dict(zip(key_list, data_list))
            r = json.dumps(doc_zip)
            print(r)

        except TypeError:
            print('TypeErrorTypeErrorTypeErrorTypeErrorTypeErrorTypeErrorTypeErrorTypeErrorTypeError')
        print('--------------------')
