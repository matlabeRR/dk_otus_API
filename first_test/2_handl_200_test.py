"""
Как умеем обрабатываем статус ответа на GET любого урла
"""

import requests


def test_answer(url_hand):
    """
    проверяем ответ урла на статус
    :param url_hand: параметр. Принимает в себя знаения параметра консоли --url, хранит в себе урл. По-умолчанию==ya.ru
    :return:
    """
    r = requests.get(url_hand)
    assert (r.status_code == 200), 'Ожидаем двухсотый статус ответа'
    assert r.raw, 'Ответ не должен быть пустым'
