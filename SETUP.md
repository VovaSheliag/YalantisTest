Доступные учетные записи

| Тип пользователя | Логин  | Пароль   |
| ---------------- |--------|----------|
| Админ            | admin  | MoS6EE8r |

# Установка

Для запуска на ПК должны быть установлены:
[Python 3.9](https://www.python.org/downloads/);
[Git](https://git-scm.com/);

Склонируйте репозиторий

```sh
$ git clone https://github.com/VovaSheliag/YalantisTest.git
```

### 1) Настройка Django

В корне проекта создайте виртуальное окружение и активируйте его

```sh
$ python -m venv “venv”
$ .\venv\Scripts\activate (для Linux: source ./venv/bin/activate)
```

#### Все последующие действия производить внутри виртуального окружения

Установите все необходимые зависимости для работы Django

```sh
$ pip install -r requirements.txt
```

#### В папке core скопируйте файл .env.example в .env

Установите все необходимые миграции, убедитесь, что был создан файл db.sqlite3

```sh
$ python manage.py makemigrations
$ python manage.py migrate
```

Запустите проект

```sh
$ python manage.py runserver
```