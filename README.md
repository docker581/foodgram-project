# foodgram-project

## Описание
Продуктовый помощник (дипломный проект)

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

### Пример файла .env
```bash
DB_ENGINE=django.db.backends.postgresql 
DB_NAME=postgres 
POSTGRES_USER=postgres 
POSTGRES_PASSWORD=postgres
DB_HOST=db 
DB_PORT=5432
```

### Запуск приложения
```bash
docker-compose up -d
```

### Создание суперпользователя
```bash
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate --noinput
docker-compose exec web python manage.py createsuperuser
```

### Подключение статики
```bash
docker-compose exec web python manage.py collectstatic --no-input
```

### Заполнение базы ингредиентов
- В админке (localhost/admin/)
- С помощью готового набора данных
```bash
docker-compose exec web python manage.py load_ingredients
```

## Автор
Докторов Денис, студент факультета Бэкенд Яндекс Практикум
