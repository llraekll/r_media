# R-Soultions
## Python 
![alt tag](https://github.com/llraekll/r-shortlinks/blob/main/images/python.png)

## Django
![alt tag](https://github.com/llraekll/r-shortlinks/blob/main/images/dj1.png)


A python app built on the framework Django, this is a social media platform performing CRUD oprations- 
* User sign-up
* User sign-in
* User sign-out
* View user profile
* Edit user profile
* Add/edit bio

![alt tag](https://github.com/llraekll/R_media/blob/main/media/login%20page.png)

Users can perform actions such as 
* Upload a post 
* View a post 
* Like a post
* Follow other users
* User also gets follow recommendations



![alt tag](https://github.com/llraekll/R_media/blob/main/media/Profile.png)
![alt tag](https://github.com/llraekll/R_media/blob/main/media/bio.png)

This repo can be installed by following the steps below

```bash
    django-admin startproject "name"
    git clone git@github.com:llraekll/r_solutions.git
    pip install -r requirements.txt
```
![alt tag](https://github.com/llraekll/FastAPI/blob/main/images/Heroku.png)
### Deploy on Heroku
```bash
    pip install whitenoise
```
In settings settings.py add 

```bash
    MIDDLEWARE = [
    # ...
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    # ...
]
```
Want forever-cacheable files and compression support? Just add this to your settings.py:

```bash
    STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
``` 
In wsgi.py file add whitenoise as application

```bash
    import os
    from whitenoise import WhiteNoise

    from django.core.wsgi import get_wsgi_application

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'r_solutions.settings')

    application = get_wsgi_application()
    application = WhiteNoise(application)
```

* Create a Procfile mentioning the app’s web server
```bash
    web: gunicorn r_solutions.wsgi --log-file - 
```

* Create a requirements.txt file for Heroku to identify the language
* Ensure there are no unused libraries mentioned in the source code
* Add and commit source code, create a Heroku remote as mentioned on Heroku
* Deploy your code 

```bash
    git add --all
    git commit -am "comment"
    git push heroku main
```
