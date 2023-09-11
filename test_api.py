# Ковтун Александр, 8-я когорта — Финальный проект. Инженер по тестированию плюс
import requests
import pytest
from api_tests.configuration import TestConfig
from api_tests.data import TestData


@pytest.fixture(scope="module")
def base_url():
    return TestData.BASE_URL


@pytest.fixture(scope="module")
def order_payload():
    return TestData.ORDER_PAYLOAD


@pytest.fixture(scope="module")
def track():
    return TestConfig.TRACK


def test_create_order(base_url, order_payload):
    url = f'{base_url}/api/v1/orders'
    payload = order_payload
    response = requests.post(url, json=payload)
    assert response.status_code == 201  # Проверяем, что заказ успешно создан
    TestConfig.TRACK = response.json().get('track')  # Сохраняем номер трека


def test_get_order_by_track(base_url, track):
    if not track:
        pytest.fail("Нет доступных номеров трека.")
    url = f'{base_url}/api/v1/orders/track?t={track}'
    response = requests.get(url)
    assert response.status_code == 200  # Проверяем, что получение заказа по треку успешно
