# Домашнее задание №3

## Создать и запустить Django-проект — 2 балла;
Для начала нужно выбрать тематику проекта. Некоторые критерии:
* В будущем мы будем делать авторизацию, поэтому пользователь должен как-то взаимодействовать с сущностями;
* Будет личный кабинет и главная страница, а так же старница сущности,
Например для каталога книг -- пользователь может авторизоваться, посмотреть страницу со всеми книгами (т.н. лента), страницу с книгами определённой категории или посмотреть страницу с полной информацией о книге. Книгу он сможет добавить в избранное.
## Реализовать «заглушки» для всех методов API, используя JsonResponse  — 3 баллов:
* Профиль;
* Список продуктов;
* Страница категории;
* и т.д.

> Реализованные заглушки 
> * Получение списка автомобилей: GET /api/cars
> * Добавление нового автомобиля: POST /api/cars
> * Получение информации об автомобиле: GET /api/cars/{car_id}
> * Изменение информации об автомобиле: PUT /api/cars/{car_id}
> * Удаление автомобиля: DELETE /api/cars/{car_id}
> * Получение списка клиентов: GET /api/customers
> * Добавление нового клиента: POST /api/customers
> * Получение информации о клиенте: GET /api/customers/{customer_id}
> * Изменение информации о клиенте: PUT /api/customers/{customer_id}
> * Удаление клиента: DELETE /api/customers/{customer_id}
> * Получение списка продаж: GET /api/sales
> * Добавление новой продажи: POST /api/sales
> * Получение информации о продаже: GET /api/sales/{sale_id}
> * Изменение информации о продаже: PUT /api/sales/{sale_id}
> * Удаление продажи: DELETE /api/sales/{sale_id}

## В конфиге nginx создать location, которое будет ходить на Django-приложение — 3 балла
На самом деле создать нужно два location:
* Курс не подразумевает вёрстку, но какое-то отображение мы хотим получить. Давайте назовём этот location /web/;
* В современных веб-приложениях реализован SPA (single page application), вёрстка отделена от логики, и требуются данные только. Такой location мы назовём /api/.
## Обрабатывать только нужные методы (GET/POST) — 2 балла.

# Домашнее задание №4

## Установить Postgres, создать нового пользователя и БД и настроить доступ — 5 баллов;
## Спроектировать базу данных проекта, подготовить модели и мигрировать их в БД — 5 баллов;
* должна присутствовать как минимум одна из связей OneToOne, ForeignKey, ManyToMany)

# Домашнее задание №5
1. Реализовать методы для:
   1. Поиска пользователей
   2. Создания персонального чата
   3. Получения списка чатов

> * Реализовал методы описанные в ДЗ №3

# Домашнее задание №6

## Установить docker и docker-compose (1 балл);
Например, как установить на [Ubuntu](https://docs.docker.com/engine/install/ubuntu/) или [MacOS](https://docs.docker.com/desktop/install/mac-install/).
## Создание Dockerfile для Django приложения (2 балла);
У нас уже есть приложение. Не забудем обновить requirements.txt с установленными питоновскими пакетами.
Нам нужно создать Dockerfile, который собрал бы образ нашего приложения. Важно помнить, что мы будем ходить в БД, как минимум.

## Создание docker-compose для проекта:
- nginx (2 балла),
- Django-приложение (2 балла)
- База данных (2 балла),

## Создание Makefile для проекта (1 балл);

Преподаватель должен иметь возможность, имея установленными только git,
docker и docker-compose склонировать проект, выполнить команды `make
migrate` и увидеть успешную миграцию.

