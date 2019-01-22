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
import json
import requests

"""connect to squarespace API"""

baseUrl = 'https://api.squarespace.com/1.0/commerce/orders'

# curl "https://api.squarespace.com/1.0/commerce/orders?modifiedAfter=2016-04-10T12:00:00Z&modifiedBefore=2016-04-15T12:30:00Z" -H "Authorization: Bearer df7d9174-295d-4730-b73d-4f97230c1838"
headers = {
    'Authorization': 'Bearer df7d9174-295d-4730-b73d-4f97230c1838',
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


key_list = ['firstName', 'lastName', 'memberNumber', 'birthDate', 'motorcycleBrandAndModel', 'email',
            'riderClass']
data_list = []

response = requests.get('https://api.squarespace.com/1.0/commerce/orders/', headers=headers, params=params)
testDict = response.json()
# customizations

custom_form_data = testDict['result'][0]['lineItems'][0]['customizations']
for each_dict in range(len(custom_form_data)):
    for label_value in custom_form_data[each_dict]:
        if label_value == 'value':
            if custom_form_data[each_dict]['label'] != 'Rider Age *':
                data_list.append(custom_form_data[each_dict][label_value])
print(data_list)
data_dict = dict(zip(key_list, data_list))
print(data_dict)
# print(single_order_data[data_point][0]['customizations'])
print('----------------')
