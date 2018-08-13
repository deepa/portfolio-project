##Setup python and django

####1. Install python3
- don’t disturb existing python2 in the system
- install python3, then make an alias to python3 for ‘python’ and to pip3 for ‘pip’ or explicitly use python3 and pip3 for all commands

####2. Install django
Use pip3 to install django and check the installations:

`	sjc-mpq47:~ dthiagar$ python
	Python 3.6.4 (v3.6.4:d48ecebad5, Dec 18 2017, 21:07:28) 
	sjc-mpq47:~ dthiagar$ django-admin --help
	Type 'django-admin help <subcommand>' for help on a specific subcommand.`

if you get this error when using django-admin:

`	Traceback (most recent call last):
  File "/usr/local/bin/django-admin", line 2, in <module>
    from django.core import management
ImportError: No module named django.core`

...django-admin is probably referring to python2 and is unable to find django (as we installed it with python3 using pip3). To fix:

`sjc-mpq47:bin dthiagar$ which django-admin
/usr/local/bin/django-admin
sjc-mpq47:bin dthiagar$ cd /usr/local/bin/
sjc-mpq47:bin dthiagar$ vi django-admin `

change the first line to refer python3 like this:

`	#!/usr/bin/env python3`

####3. Setup the virtual environment

- Install virtualenv
pip3 install virtualenv

- Create a virtual environment and switch to it

`$ virtualenv myvenv
$ source myvenv/bin/activate
(myvenv) sjc-mpq47:udemy-django2 dthiagar$ python
Python 3.6.4 (v3.6.4:d48ecebad5, Dec 18 2017, 21:07:28) `

Check python and django installations in the virtual environment. Proceed if everything looks fine, otherwise install django again in the virtual environment.

##Portfolio App
###Get started with the Portfolio app

* Enter the virtual environment. Use django-admin to start a project

`django-admin startproject portfolio`

* Rename the parent directory to portfolio-project to avoid confusion. Then import the project to the text editor.

* Initialize git and add .gitignore

* Install postgres. For Mac, postgres app is a easy way to use postgres. Install it from postgres website. Then create a database called portfolio. Connect postgres to the python project by updating settings.py file inside the project (the field DATABASES)

* Add apps for blog and job. This adds directory structures for blog and jobs and configuration files

`python manage.py startapp blog
python manage.py startapp jobs`

* Create a superuser for the django-admin interface to add new models and run the server. Then go to the django admin web interface at http://localhost:8000/admin/ and login with the credentials created

`python manage.py createsuperuser
python manage.py runserver`

* To work with images, install Pillows using pip3. Configure settings.py to specify image directories (MEDIA_ROOT and MEDIA_URL) and add the URL patterns for the images by updating urls.py in the project (the field urlpatterns)

* Configure the apps blog and job

For each app:

 * In the models.py file that got generated, add the app class and the fields
 * Add the model to the project by updating settings.py and adding the apps in INSTALLED_APPS field
 * Create and make migrations:

`python manage.py makemigrations
python manage.py migrate`

 * Add the models to Admin interface 

* Go back to the admin interface to verify that everything runs fine and there are options to add new objects for the new models added

###Add pages to the app
* Add a new function in jobs/views.py to render the homepage

`def home(request):
    return render(request, 'jobs/home.html')`

* Add a new urlpattern to urls.py in the project to allow a new page called home to our web app, and 

`import jobs.views
path('', jobs.views.home, name='home')`

* Add a new html page at jobs/templates/jobs/home.html






