
## Online Shop Django



<img src="https://img.shields.io/badge/python-3.7-purple">  <img src="https://img.shields.io/badge/django-3.2.10-blueviolet">  <img src="https://img.shields.io/badge/licence-MIT-blue">  <img src="https://img.shields.io/badge/SQLite-green">

# About
An online store project developed with Python and Django. It includes user registration and information storage for seamless order delivery. The project also features an admin panel for managing users, products, and categories, providing full control over the store's operations. It uses SQLite for storing the data.

# Installation

1. Create a virtual environment and activate it:
```
python -m venv venv
source venv/bin/activate
```
2. Install dependencies:
```
pip install -r requirements.txt
```
3. Run migrations and load data into the database:
```
python manage.py migrate
python manage.py loaddata data.json
```
4. Create administrator user:
```
python manage.py createsuperuser
```
5. Run the server:
```
python manage.py runserver
```

Open browser and go to http://127.0.0.1:8000/admin/. Enter your administrator username and password to log into your store control panel.

# Developers
- [Hewins Bogdan](https://github.com/AzaTheGreat)

# License
This project is distributed under the MIT license.
