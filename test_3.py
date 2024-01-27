# Игорь Корб, 12-я когорта — Финальный проект. Инженер по тестированию плюс

import configuration
import requests
import data



def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.ORDERS,
                         json=body,
                         headers=data.headers)

def get_order(track):
    return requests.get(configuration.URL_SERVICE + configuration.ORDER_TRACK + str(track))

def test():
  response = post_new_order(data.order_body)
  track = response.json()["track"]
  newres = get_order(track)
  if newres.status_code == 200:
    print(" По треку заказа можно получить данные о заказе")



