# REST API for car park with drivers

Available accounts

| User type | Login | Password |
|-----------|-------|----------|
| Admin     | admin | MoS6EE8r |

# Installation

To run on a PC, must be installed:
[Python 3.9](https://www.python.org/downloads/);
[Git](https://git-scm.com/);

Clone repository

```sh
$ git clone https://github.com/VovaSheliag/YalantisTest.git
```

### 1) Django setup

At the root of the project, create a virtual environment and activate it

```sh
$ python -m venv “venv”
$ .\venv\Scripts\activate (for Linux: source ./venv/bin/activate)
```

#### All subsequent actions should be performed inside the virtual environment.

Install all required dependencies for Django to work

```sh
$ pip install -r requirements.txt
```

#### In the core folder, copy the .env.example file to .env

Install all required migrations, make sure db.sqlite3 file was generated

```sh
$ python manage.py makemigrations
$ python manage.py migrate
```

Run the project

```sh
$ python manage.py runserver
```