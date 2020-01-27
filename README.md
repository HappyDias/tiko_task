
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

## Running the project

### Running the dev server

The user is required to have django and python installed (preferrably python 3 and django 3), please visit https://www.python.org/downloads/ and https://www.djangoproject.com/download/ to install these dependencies.

Once the above dependencies are installed, you cam run the development server by opening a command prompt, navigating to the repository folder and running the following command

```
python manage.py runserver 
```

It is NOT recommended that this server be used in a production environment, this is only for checking how the application is working.

### Deploying the application

Django applications like these can be run in a variety of ways on a production environment, visit https://docs.djangoproject.com/en/3.0/howto/deployment/ for more information on deployment

## Comments

1. Since the project states that two pages are to be supplied, I created an app with two views, each of wich returns a template, each template will, respectively, include the required functionality of each page (landing page and graph page).

2. Could not get app static files to work for some reason, all static files (JS, CSS, etc...) will be served from a global base folder called `static`, since this is a single app project it is not a big issue, in a real life larger project, I would have to fix the app static files.

