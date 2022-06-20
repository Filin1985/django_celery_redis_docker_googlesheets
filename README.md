# django_celery_redis_docker_googlesheets

Проект бере данные из таблицы googlesheets с исипользованием google api и сохраняет данные в модель django.
Настроено обновление данных каждую минуту с помощью тасков Celery.
Сумма в долларах из таблицы конвертируется в рубли с использованием api ЦБ РФ

В проекте использовались:
* Django
* Celery
* Redis
* Postgres
* Docker

## Запуск проекта
```
docker-compose up --build
```
