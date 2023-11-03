# Django CSV Loader Usage Instructions

This `loader` app for Django allows you to import CSV data directly into your Django models and makes it accessible through the Django admin panel. Here's how to use it:

### Prerequisites

Make sure you have the following requirements installed:
- Python 3.x
- Django 3.x or higher

### Setup

1. Download the `django-loader` app from the repository:

```bash
git clone https://github.com/AleksandarBuk/django-loader.git
```
### Setup

1. Clone the repository to your local machine.
2. Navigate to the root directory of your Django project where the `manage.py` file is located.
3. Ensure the `loader` app is included in the `INSTALLED_APPS` section of your `settings.py` file:

```python
# settings.py

INSTALLED_APPS = [
    'loader',
]
```
Run migrations to initialize your database schema:

```python
python manage.py migrate
```

## Usage
```bash 
python manage.py import_csv loader/data/test_data.csv
```

## Create an Admin User
Create a superuser to access the Django admin interface:

```bash
python manage.py createsuperuser
```
## View the results
Start the Django development server and navigate to the admin panel to view the imported data:
```bash
`python manage.py runserver`
```
Then, open your web browser and go to `http://localhost:8000/admin`.

## Conclusion
After logging in with the superuser account, you should see the data imported from test_data.csv in the relevant model section within the Django admin site.
