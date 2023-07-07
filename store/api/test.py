import requests

# Замените URL на ваш эндпоинт API
url = 'http://127.0.0.1:8000/api/products_room/1/'

# Отправляем POST-запрос для добавления товара в корзину
response = requests.post(url)

# Проверяем статус-код ответа
if response.status_code == 201:
    print('Товар успешно добавлен в корзину.')
else:
    print('Ошибка при добавлении товара в корзину.')