"""
основной файл с тестами по API https://dog.ceo/dog-api/
"""

from typing import Any, Union
import requests
import pytest


#   создадим функцию, которая должна получать список всех пород и их же возвращать
def all_breed_list():
    """
    :return: keys - список всех пород
    """
    a = 'https://dog.ceo/api/breeds/list/all'
    a = requests.get(a)
    a = a.json()
    keys = []
    for breeds in (a['message']):
        keys += [breeds]
    return keys


#   создадим функцию, которая должна возвращать словарь только тех пород, у которых есть сабпороды
def sub_dict():
    """
    :return: sub - словарь только тех пород, у которых есть сабпороды
    """
    a = "https://dog.ceo/api/breeds/list/all"
    a = requests.get(a)
    a = a.json()
    sub = {}
    for breed in all_breed_list():
        if a['message'].setdefault(breed):
            sub.update({breed: a['message'].setdefault(breed)})
    return sub


# тестируем get_all_breeds
def test_all_br(base_url_test, all_breeds_test):
    """
    проверяем получение всех пород и саб-пород
    :param base_url_test: фикстура, основа урла
    :param all_breeds_test: фикстура, продолжает базу урла
    :return:
    """
    a = base_url_test + all_breeds_test
    a = requests.get(a)
    a = a.json()
    print(a)
    assert (isinstance(a, dict)) and (a is not None), 'Переменная должна иметь тип dict и быть непустой'


#  проверяем, есть ли случайное значение в списке всех пород
def test_have_breed_in_list(base_url_test, rand_one_test):
    """
    проверяем наличие рандомной породы в списке всех пород
    :param base_url_test: фикстура, основа урла
    :param rand_one_test: фикстура, продолжает базу урла
    :return:
    """
    r = base_url_test + rand_one_test
    r = requests.get(r)
    r = r.json()
    completed = False
    for key in all_breed_list():
        if r['message'].find(key) != -1:
            completed = True
            break
    assert completed, 'Найдено ли значение в списке всех пород'


# тестируем random breeds
def test_rnd_br(base_url_test, rand_one_test):
    """
    проверяем длину ответ получения рандомной породы
    :param base_url_test: фикстура, основа урла
    :param rand_one_test: фикстура, продолжает базу урла
    :return:
    """
    r = base_url_test + rand_one_test
    r = requests.get(r)
    r = r.json()
    print(r)
    assert (isinstance(r, dict)) and (r is not None) and (len(r) == 2), 'Переменная должна иметь тип dict и иметь длину ==2'


# random image с параметризацией от 1 до 50
@pytest.mark.parametrize('number_of_images', ([i for i in range(1, 50)]))
def test_rnd_param(base_url_test, rand_one_test, number_of_images):
    """
    проверяем работоспособность возможность получения кол-ва рандомных изображений
    :param base_url_test: фикстура, основа урла
    :param rand_one_test: фикстура, продолжает базу урла
    :param number_of_images: параметр, кол-во изображений
    :return:
    """
    r = base_url_test + rand_one_test + '/' + str(number_of_images)
    print(number_of_images)
    r = requests.get(r)
    r = r.json()
    # print(r)
    assert (number_of_images == len(r['message'])) and (r['status'] == 'success'), \
        'Длина списка должна быть == кол-ву изображений и статус запроса == выполнен'


# моя параметризованная прелесть, проверяющая все фотки пород, имеющих саб-породы
@pytest.mark.parametrize('bre, sub', [(x, y) for x in sub_dict() for y in sub_dict()[x]])
def test_sub(base_url_test, bre, sub):
    """
    проверяем наличие фотографий каждой сабпороды
    :param base_url_test: фикстура, основа урла
    :param bre: параметр, из функции sub_dict получает ключи соответствующего словаря
    :param sub: параметр, из функции sub_dict получает ключи соответствующего словаря
    :return:
    """
    r: Union[str, Any] = base_url_test + 'breed/' + bre + '/' + sub + '/images'
    r = requests.get(r)
    r = r.json()
    assert (r['message'] is not None) and (r['status'] == 'success'), \
        'тест ответа по всем ссылкам не пустой и статус запроса == выполнен'
