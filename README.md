# Installation

1. Create a virtual environment and activate it
```
python -m venv venv
source venv/bin/activate
```
2. Install dependencies
```
pip install -r requirements.txt
```
3. Run migrations and load data into the database
```
python manage.py migrate
python manage.py loaddata data.json
```
4. Create administrator user
```
python manage.py createsuperuser
```
5. Run the server
```
python manage.py runserver
```

Open browser and go to  http://127.0.0.1:8000/admin/. Enter your administrator username and password to log into your store control panel.

# Done!