# from main.celery import app as celery_app
# from .models import Wallet
# import requests
#
# @celery_app.task
# def user_balance_task(user_id):
#     try:
#         user = User.objects.get(id=user_id)
#         wallet = Wallet.objects.get(user=user)
#         balance = wallet.balance
#     except User.DoesNotExist:
#         # Обработка случая, когда пользователя не существует
#         balance = 0
#     except Wallet.DoesNotExist:
#         # Обработка случая, когда кошелек не существует
#         balance = 0
#
#     url = 'https://belarusbank.by/api/kursExchange'
#     city = 'Минск'
#     response = requests.get(url, params={'city': city})
#
#     if response.status_code == 200:
#         data = response.json()
#         # Извлечение значений курса валют из полученных данных
#         usd_in = data[0]['USD_in']
#         usd_out = data[0]['USD_out']
#         eur_in = data[0]['EUR_in']
#         eur_out = data[0]['EUR_out']
#         rub_in = data[0]['RUB_in']
#         rub_out = data[0]['RUB_out']
#
#         # Вывод результатов асинхронной задачи в лог
#         print(f"Баланс пользователя {user_id}: {balance}")
#         print(f"Курс доллара: Покупка - {usd_in}, Продажа - {usd_out}")
#         print(f"Курс евро: Покупка - {eur_in}, Продажа - {eur_out}")
#         print(f"Курс российского рубля: Покупка - {rub_in}, Продажа - {rub_out}")
#     else:
#         # Обработка ошибки при получении данных из API
#         print(f"Ошибка при получении данных о курсе валют")
#
#     # Возвращаем результаты асинхронной задачи
#     return {
#         'balance': balance,
#         'usd_in': usd_in,
#         'usd_out': usd_out,
#         'eur_in': eur_in,
#         'eur_out': eur_out,
#         'rub_in': rub_in,
#         'rub_out': rub_out
#     }
