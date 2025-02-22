import os
import sys

import requests
from urllib.parse import urlencode


def get_map_image(search: str) -> str:
    coordinates, span = get_coordinates(search)

    params = {'ll': ','.join(map(str, coordinates)),
              'spn': ','.join(map(str, span))}
    query_string = urlencode(params)
    return show_map(query_string)



def show_map(ll_spn=None) -> str:
    server_address = 'https://static-maps.yandex.ru/v1?'
    api_key = 'f3a0fe3a-b07e-4840-a1da-06f18b2ddf13'
    # Готовим запрос.

    map_request = f"{server_address}{ll_spn}&apikey={api_key}"
    response = requests.get(map_request)

    if not response:
        print("Ошибка выполнения запроса:")
        print(map_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit(1)

    # Запишем полученное изображение в файл.
    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)

    return map_file


def get_coordinates(geocode: str) -> tuple[tuple[float, float], tuple[float, float]]:
    server_address = 'http://geocode-maps.yandex.ru/1.x'
    api_key = '8013b162-6b42-4997-9691-77b7074026e0'
    # Готовим запрос.
    geocoder_request = f'{server_address}?apikey={api_key}&geocode={geocode}&format=json'

    # Выполняем запрос.
    response = requests.get(geocoder_request)
    if not response:
        print("Ошибка выполнения запроса:")
        print(geocoder_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")
    else:
        # Преобразуем ответ в json-объект
        json_response = response.json()

        # Получаем первый топоним из ответа геокодера.
        # Согласно описанию ответа, он находится по следующему пути:
        toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
        # Полный адрес топонима:
        toponym_address = toponym["metaDataProperty"]["GeocoderMetaData"]["text"]
        # Координаты центра топонима:
        toponym_coodrinates = toponym["Point"]["pos"]
        # Печатаем извлечённые из ответа поля:

        position = tuple(map(float, toponym['Point']['pos'].split()))
        bounded_by = tuple(map(float, toponym['boundedBy']['Envelope']['lowerCorner'].split()))
        span = (
            abs(position[0] - bounded_by[0]) / 0.6,
            abs(position[1] - bounded_by[1]) / 0.6,
        )
        return position, span

