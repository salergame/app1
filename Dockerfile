FROM python:3.11.5

ENV PYTHONUNBUFFERED 1

# Здесь можно добавлять пакеты, которые необходимы для работы приложения
RUN apt update && apt install -y python3-dev

WORKDIR /code

# Сначала копируем requirements.txt, для того, чтобы образ собирался быстрее (см. слои докера)
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# Далее копируем сам код приложения
COPY . /code/
WORKDIR /code/

EXPOSE 8000
#3040911672