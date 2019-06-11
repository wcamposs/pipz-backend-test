# pipz-backend-test
My test for the back-end internship at Pipz Automation

## Getting Started
Initially I recommend that you create an isolated environment using virtualenv, to install and create an isolated environment, use the [documentation](https://virtualenv.pypa.io/en/latest/)

Once inside the virtual environment, clone the repository using the command below:
```
$ git clone https://github.com/wcamposs/pipz-backend-test
```
## Installing Required Packages
As stated in *requirements.txt*, you will need the following packages:
- Django==2.2.2
- django-rest-auth==0.9.5
- djangorestframework==3.9.4

Assuming you have the Pip package installed and uses Python 3, install the necessary packages through the following commands:
```
$ pip install django
```
```
$ pip install django-rest-auth
```
```
$ pip install djangorestframework
```

## Running the Application
Before running the application, you must create initial migrations for the database. Therefore, use the following commands:
```
$ python manage.py makemigrations
```
```
$ python manage.py migrate
```

After migrating, you need to create a superuser (composed of user, email and password):
```
$ python manage.py createsuperuser
```

Then start the application using the command:
```
$ python manage.py runserver
```

## Useful URLs
When starting the application, the API will be available at http://127.0.0.1:8000/ by default, however, these are the urls used in the API:
```
http://127.0.0.1:8000/school/login/

http://127.0.0.1:8000/school/logout/

http://127.0.0.1:8000/admin/

http://127.0.0.1:8000/school/students/

http://127.0.0.1:8000/school/teachers/
```
