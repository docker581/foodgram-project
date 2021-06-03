# foodgram-project

## Описание проекта
Продуктовый помощник (дипломный проект)

## Статус
На сдаче 1 части

## Стек технологий
- Python 3.8.5
- Django 3.0.5
- Django Rest Framework (DRF) 3.12.4
- Docker-compose 3.3
- Postgres 12.4
- Nginx 1.19.3
- Gunicorn 20.0.4

## Установка docker
https://docs.docker.com/engine/install/

## Команды
### Клонирование репозитория
```bash
git clone https://github.com/docker581/foodgram-project
```

### Запуск приложения
```bash
docker-compose up -d
```

### Создание суперпользователя
```bash
docker-compose exec web python manage.py migrate --noinput
```
```bash
docker-compose exec web python manage.py createsuperuser
```

### Заполнение базы ингредиентов
- В админке (localhost/admin/)
- С помощью готового набора данных
```bash
docker-compose exec web python manage.py load_ingredients
```

## Автор
Докторов Денис, студент факультета Бэкенд Яндекс Практикум
