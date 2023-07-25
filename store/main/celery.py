# import os
# from celery import Celery
#
# # Установите переменную окружения для указания файла настроек Django
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')
#
# # Создайте экземпляр Celery
# app = Celery('celery_app')
#
# # Загрузите настройки из файла settings.py
# app.config_from_object('django.conf:settings', namespace='CELERY')
#
# # Автоматическое обнаружение и регистрация задач в приложениях Django
# app.autodiscover_tasks()