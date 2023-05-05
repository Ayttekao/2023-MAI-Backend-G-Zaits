# использование образа Python
FROM python:3.10

# установка переменной окружения
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE carProject.settings

# создание директории для кода приложения
RUN mkdir /app

# Установка рабочей директории
WORKDIR /app

# Копирование зависимостей проекта в рабочую директорию
COPY requirements.txt .

# Установка зависимостей
RUN pip install -r requirements.txt

# Копирование файлов проекта в рабочую директорию
COPY ./lab_03 /app/