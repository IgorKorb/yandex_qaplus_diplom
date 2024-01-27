# Игорь Корб, 12-я когорта — Финальный проект. Инженер по тестированию плюс

import data
import func


def test_get_order_by_track_success():
  response = func.post_new_order(data.order_body)
  track = response.json()["track"]
  newres = func.get_order(track)
  assert newres.status_code == 200