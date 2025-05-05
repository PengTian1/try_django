# This is for Django Beginners

### Templates: Views Generating Response based on Templates

* `myproject/views.py`: render the templates

        def homepage(request):
            context = {
                'title': 'Welcome to My Django App',
                'message': 'This is the homepage of my Django application.',
            }
            return render(request, 'home.html', context)
    
    - `request`: http request from user.
    - `home.html`: path of the template. Django looks for templates in `templates/` folder of each installed app. So it's suggested to use format `app_name/template_name.html`. Here we are using additional template directories to show how to configure it. 
    - `context`: data passed to the template.

* `templates/home.html`: A template contains static parts and some special syntax(variables and logic) describing how dynamic content will be inserted.

        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            {% if title %} <!-- Check if title is provided -->
                <title>{{ title }}</title>
            {% else %}
                <title>Home</title>
            {% endif %}
        </head>
        <body>
            <h1>{{ message }}</h1>
        </body>
        </html>

    - use `{{ variable }}` to display variables 
    - use `{% %}` to control structure

* `myproject/settings.py`: make sure the additional template dir is added as below:

        TEMPLATES = [
            {
                'BACKEND': 'django.template.backends.django.DjangoTemplates',
                'DIRS': ['templates'],  # Add your templates directory here
                'APP_DIRS': True,
                'OPTIONS': {
                    'context_processors': [
                        'django.template.context_processors.debug',
                        'django.template.context_processors.request',
                        'django.contrib.auth.context_processors.auth',
                        'django.contrib.messages.context_processors.messages',
                    ],
                },
            },
        ]

* `static/css/style.css`: Configure style here

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            min-height: 100vh;
            display: grid;
            place-content: center;
            font-size: 1rem;
            background-color: black;
            color: whitesmoke;
        }

        h1, p {
            text-align: center;
        }
* `myproject/settings.py`: tell Django where's the folder for static assets.

        STATIC_URL = 'static/'
        STATICFILES_DIRS = [
            BASE_DIR / "static",
        ]

* `templates/home.html` link style

        <!DOCTYPE html>
        {% load static %}
        <html lang="en">
        <head>
            ...
            <link rel="stylesheet" href="{% static 'css/style.css' %}">
        </head>
        ...

* start the server to validate the generated html

    ![image info](template_01.png)

* Sample to link JavaScript
  - `static/js/main.js` 

        console.log('this is JS from your Home page')

  - `templates/home.html`

        <!DOCTYPE html>
        {% load static %}
        <html lang="en">
        <head>
            ...
            <script src="{% static 'js/main.js' %}" defer></script>
        </head>
        ...

    defer: wait until all of the page is loaded and then it loads the script

  - validate:

    ![image info](template_js.png)

















