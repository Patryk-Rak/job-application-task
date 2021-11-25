# Advertisement Portal
##Job application task
#

### Small web app that contains basic operations in Django, REST API and Angular frameworks.



The entire project consists of two folders - Backend and frontent side.
Applications backend is created on Django Framework with a
help of packages such as Pillow,
Django Rest Framework and Django Cors Headers.
Backend files also contains simple html templates that works as frontend if
we run project through Djangos manage.py file.

Frontend part is created using Angular latest version,
and thanks to django Cors Headers package this part of project
can communicate with backend through Django REST Api and
get informations from database.

I decided to use at the end SQLite3 as my database structure because of simplicity
when we want to migrate models, but application was also tested on PostgreSQL.
## Features

- Main page that contains most of the informations from database records - categories listed in order and offers filtered by pinned categories.
- Access to Django Administration - one of the ways to customize content in Categories and Offers database tables, including adding new records, editing and deleting existing ones.
- Access to Django REST Api Framework - part of backend used for data serialization, another way to look into database and manipulate tables. Also helps with connecting to angular and send back informations about tables content to show.




> I tried my best to implement every needed aspect from task,
> but there's lot's of extra features that wasn't added to final
> version of app, mostly because of time and unfinished / not fully
> working aspects like factory_boy library implementation or angular frontend offer-detail-page.


## Preview

![Frontpage](https://i.imgur.com/zCbqRDn.png)
Homepage that contains listed categories - after chosing one from list, offers will update
and show these only filtered by this category. After clicking on offers,
detail-page will show up, containing all informations about offer.

![Frontpage](https://i.imgur.com/MgiZIUT.png)
Django Administration page. Contains informations about database tables and records. Fully editable.

![Frontpage](https://i.imgur.com/bGxPxcx.png)
Django REST Api Framework. Mixins and ViewSets were used to generate data. Also editable.

![Frontpage](https://i.imgur.com/GfkOabS.png)
Angular Version of frontend.

## Navigation
1. Backend Server
- http://127.0.0.1:8000/ - main page with all offers listed
- http://127.0.0.1:8000/<category_name> - main page, but with filtered offers by category in slug
- http://127.0.0.1:8000/admin - Django Administration site
- http://127.0.0.1:8000/api/offers - Listed offers in REST Api Framework
- http://127.0.0.1:8000/api/offers/<id> - Picked one offer by ID. It also contains forms for CRUD
- http://127.0.0.1:8000/api/categories - Listed categories in REST Api Framework
- http://127.0.0.1:8000/api/categories/<id> - Picked one category by ID. It also contains forms for CRUD

2. Backend Server

- http://localhost:4200/ - main page, contains only empty template
- http://localhost:4200/offers - page with listed categories and offers

## Tech-Stack

Advertisement Portal uses a number of open source packages and frameworks to work properly:

- Python - 3.9.2 version
- Django - 3.2.9 version
- django-decouple - 2.1 version - helps with using .env file to read sensitive data that can't be held on git.
- Pillow - 8.4.0 version - package that allows adding images to offers
- Django-Rest-Framework - 3.12.4
- Django-cors-headers - 3.10.0 - A Django App that adds Cross-Origin Resource Sharing (CORS) headers to responses. This allows in-browser requests to your Django application from other origins. 
- Angular CLI - 13.0.3 version
- Node - 16.13.0 version
- Package Manager npm - 8.1.4 version



## Installation

###1.  Installation backend side of project

1. Download project


2. Open job-interview-task-backend file in IDE, create virtualenv and install the dependencies from requirements.txt
```sh
- virtualenv venv
- pip install -r path_to_your requirements.txt
```
3. Make a new file called:
>.env

Directly inside job-interview-task-backend file, then fill this file with this code:
```sh
DEBUG=True
TEMPLATE_DEBUG=True
SECRET_KEY=my-secret-key
```

This project use SQLite3 data service, so we don't need to set up database in settings, only :
4. Start the server by following command.
```sh
- python manage.py makemigrations
- python manage.py migrate 
- python manage.py runserver
```
manage.py is in the location:
> job-interview-task-backend/advertisement_portal/


5. To access Django Administration page, we need to create superuser with command:
```sh
- python manage.py createsuperuser
```
I created custom user model, so during registration it will ask for email and password, eg. test@test.com, pass: 1234 will work.
###2.  Installation frontend side of project

1. Download project


2. Open job-interview-task-frontend file in IDE, make sure you have installed NodeJS and @angular/CLI, then install packages:
```sh
npm install (with no args, in package dir)
npm install [<@scope>/]<name>
npm install [<@scope>/]<name>@<tag>
npm install [<@scope>/]<name>@<version>
npm install [<@scope>/]<name>@<version range>
npm install <git-host>:<git-user>/<repo-name>
npm install <git repo url>
npm install <tarball file>
npm install <tarball url>
npm install <folder>

aliases: npm i, npm add
common options: [-P|--save-prod|-D|--save-dev|-O|--save-optional] [-E|--save-exact] [-B|--save-bundle] [--no-save] [--dry-run]
```
3. use
```sh
ng serve
```
in 
>/job-interview-task-frontend/
 
folder to run server.
## Creators
   
- [Patryk Rak] 


   [Patryk Rak]: <https://github.com/Patryk-Rak>
