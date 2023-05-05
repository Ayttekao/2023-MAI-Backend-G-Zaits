# переменные
PROJECT_NAME=cardealer

# команды
build:
    docker-compose build

up:
    docker-compose up

down:
    docker-compose down

restart:
    make down
    make up

migrate:
    docker-compose run --rm web python manage.py migrate

createsuperuser:
    docker-compose run --rm web python manage.py createsuperuser

shell:
    docker-compose run --rm web python manage.py shell

logs:
    docker-compose logs -f