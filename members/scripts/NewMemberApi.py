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

list_data_needed = ["id"]

response = requests.get('https://api.squarespace.com/1.0/commerce/orders/', headers=headers, params=params)
testDict = response.json()
order_list = (testDict['result'])
print(order_list)
for order in range(len(order_list)):
    single_order_data = order_list[order]
    for data_point in list_data_needed:
        print(single_order_data[data_point])
        print('----------------')
