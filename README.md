
# tiko_task

Task fort Tiko Energy

## Requested task

Here is the task. Feel free to ask Marcelo or I questions via Skype or email.

 

1. Build a new Django project with 2 pages:
	* A welcome page with a link to the “graph” page
	* A graph page displaying a real time chart (see point 2)

2. Build the “graph” page:
	* Include a graph library (e.g. D3, chart.js, highcharts)
	* Plot the real time length of the “joke” element of this API (1 Pull per second is requested): http://api.icndb.com/jokes/random

Please send us a build when you have this part complete.

Optional tasks: include as many as you have time / energy 😊

3. Add a login page to this django project (using standard django middleware)
4. Add linting for the JS files with eslint
5. Add a CSS pre-processor like Sass, Less etc
6. Implement a watch task to process CSS and lint JS on changes

Notes:

You are encouraged to use Bootstrap: http://getbootstrap.com/ and you can follow the Django tutorial 

Useful links:

* https://www.djangoproject.com/

* https://www.highcharts.com/

* https://www.chartjs.org/

* http://d3js.org/

## Running the Project

### Dependencies

The user is required to have django and python installed (preferrably python 3 and django 3), please visit https://www.python.org/downloads/ and https://www.djangoproject.com/download/ to install these dependencies.

The user is required to install these dependecies before running the project. Please go throw each of the bullet points that list the main dependencies and provide links for how to install them:

1. [Python](https://www.python.org/downloads/)
2. [Django](https://www.djangoproject.com/download/)
3. [Nodejs](https://nodejs.org/en/download/)

Apart from these main dependencies, the user is required to install specific dependencies for node and python:

#### Node.js Dependencies

This project uses nodejs third-party modules to handle javascript specific tasks, to install these third party modules, run a shell and navigate to the project base folder, once there run the following command

```
npm install
```

NOTE: This requires nodejs to be installed on your system!

#### Python Dependencies

This project uses third-party python libraries, dependencies are managed by another third-party library called `pipenv`. If you don't have `pipenv` installed in your system, first run the following command (you can access [this site](https://github.com/pypa/pipenv) to get more information about installing pipenv):

```
pip install pipenv
```

Once `pipenv` is installed in your system, navigate to this project's base folder and run the following commands:

```
pipenv shell
pipenv install
```

NOTE: This requires python to be installed on your system!

### Run Migrations

If you're running this application for the first time, you will not have the required database structure to handle user authentication. Django provides a tool to create said dataabse with the required structure. Navigate to the project's base folder and run the following command:

```
python manage.py migrate 
```

This should create the required database structure to hanle authentication

### Create Users

If you're running this application for the first time, you will not have any users to authenticate access to the app. You must first create a superuser to handle all top level administrative tasks. To create the superuser, start a shell and navigate to the projects base folder. Once there, run the following command:

```
python manage.py createsuperuser
```

And follow the prompts provided to create the superuser. This user can also be used as a regular user, though doing this is highly discouraged. With this superuser created, you can access the django admin site to create more users. With the dev server running (see [Run Development Server](#run-dev-server)), you can access the admin site via http://127.0.0.1:8000/admin and log in with your newly created superuser to access an interactive application that helps you perform administrator tasks, like creating new users.

### Run Development Server

Django comes with a development server that eases the process of development. To run this server, navigate to the project's base folder and run the following command:

```
python manage.py dynamic_web_server
```

This runs a special development server that watches for changes not only in your python files, but also on your static files (JS, CSS) and performs automated checking of said files for errors.

After running the previous command, you should be able to access the app on http://127.0.0.1:8000/

It is NOT recommended that this server be used in a production environment, this is only for checking how the application is working.

### Deploying the Application

Django projects can be run in a variety of ways on a production environment, visit https://docs.djangoproject.com/en/3.0/howto/deployment/ for more information on deploying a django project.

## Comments

1. Since the project states that two pages are to be supplied, I created an app with two views, each of wich returns a template, each template will, respectively, include the required functionality of each page (landing page and graph page).

2. Could not get app static files to work for some reason, all static files (JS, CSS, etc...) will be served from a global base folder called `static`, since this is a single app project it is not a big issue, in a real life larger project, I would have to fix the app static files.

3. I redirect non-authenticated requests to the admin login page, otherwise I would have to create a new login page that would make all the request for authentication. In a real-world scenario this would be the way to go, but since this is not explicitely required, I am keeping it simple.

4. Since the task request requested ESLint to be used, there was no getting around puting node.js scripts in this project. I had hoped of doing this in pure python but unfortunately had to add the Node.js dependency

5. Since Node is dealing with the JS linting, I went ahead and implemented sass as a Node script as well, this way we have Node running tasks that are aimed at the frontend files and python/django doing exclusively backend tasks.

6. For the watch task I could have implemented something using gulp, or grunt task using Node and that would have gone with the phylosophy discussed in the previous point, however, it would have required more code. Thus I simply implemented a python watchdog class that checks for new files and changes in the static folder. Watchdog was triggering twice but this seems to be a long running issue in Windows so I implemented a time check that prevents changes younger than 1s to be registered.