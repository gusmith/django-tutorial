# django-tutorial

Learning Django framework

## Links

Use the [pythontutorial.net](https://www.pythontutorial.net/django-tutorial/getting-started-with-django/) tutorial to learn.

### Useful links

- [template builtins](https://docs.djangoproject.com/en/4.2/ref/templates/builtins/) lik to Django built-in template tags and filters

## Development

Use poetry, and python 3.12.2 locally. Not tested with anything else.

### Bootstrap

Command to create a new Django project:

```shell
poetry run django-admin startproject django_project
```

### Run development server

```shell
poetry run python manage.py runserver
```

### Create a new Django application

```shell
poetry run python manage.py startapp blog
```

### Code formatter and linter

```shell
poetry run ruff format
poetry run ruff check --fix
```

### Make model migrations

Create the migration scripts:

```shell
poetry run python manage.py makemigrations
```

See the migration:

```shell
poetry run python manage.py sqlmigrate blog 0001
```

Run the migration:

```shell
poetry run python manage.py migrate
```

### Create a super user

```shell
poetry run python manage.py createsuperuser
```
