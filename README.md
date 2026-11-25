# Django Course Exercises

My exercises from a Django course on Udemy. A small project that covers the basics: URL routing with parameters, views, templates, static images, forms and custom error pages.

## What it covers

- Function-based views and URL routing
- A URL with typed parameters: `/add/<a>/<b>` adds two numbers
- Templates with Bootstrap, and a page that shows static images
- An HTML form submitted with POST, and a Django `Form` class with validation
- A custom 404 page

## Pages

| Path | What it does |
| --- | --- |
| `/` | Home page |
| `/second/` | A second template page |
| `/imagepage/` | Page with static images |
| `/add/<a>/<b>` | Adds two numbers from the URL |
| `/myform/` | HTML form, submitted to `/submitform/` |
| `/newform/` | Django form class (title, subject, email) |

## Built with

- Python 3, Django 4.2
- SQLite

## Run it locally

```bash
git clone https://github.com/hamzakhalem/django-udemy-course.git
cd django-udemy-course
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install django
export DJANGO_SECRET_KEY="any-long-random-string"   # PowerShell: $env:DJANGO_SECRET_KEY="..."
cd myproject
python manage.py migrate
python manage.py runserver
```

`DEBUG` is off in the settings so the custom 404 page shows. Set `DEBUG = True` in `myproject/settings.py` to get Django's debug pages while developing.

## Project structure

```
myproject/
  myproject/   Settings and root URLs (custom 404 handler)
  myapp/       Views, forms and templates
```
