import configuration
import requests
import data

def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.ORDERS,
                         json=body,
                         headers=data.headers)

def get_order(track):
    return requests.get(configuration.URL_SERVICE + configuration.ORDER_TRACK + str(track))