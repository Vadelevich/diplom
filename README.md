# Сайт компании медицинской диагностики.

### Задача

В рамках проекта мне необходимо было сверстать и подключить к админке сайт. Для выполнения задачи обязательно использовать Django и Bootstrap.
Из админ панели можно редактировать главный раздел (добавлять/удалять специализации, врачей), редактировать галлерею, вести блог.
Сайт позволяет пользователям регистрироваться, а также оформлять подписку на рассылку новостей или получить бесплатное обследование.  


### Basic system requirements:

- Python 3.11
- PostgreSQL  14.7 
- Django 4.2
- Зависимости (Python) из requirements.txt


### Build & Launch

```bash

git clone git@github.com:Vadelevich/diplom.git
cd diplom
```

Ставим зависимости и создаем БД:

```bash

pip3 install -r requirements.txt
psql -U postgres 
pip3 install -r requirements.txt
psql -U postgres 
CREATE DATABASE diagnostic;
/q
```
При необходимости изменяем настройки DATABASES в /config/settings.py
Создаем суперпользователя:
```bash

python3 manage.py createsuperuser
```
к примеру (логин/пароль): admin@test.ru:admin
Выполняем миграции и запускаем тестовый сервер:
```bash

python3 manage.py migrate
python3 manage.py runserver
```
