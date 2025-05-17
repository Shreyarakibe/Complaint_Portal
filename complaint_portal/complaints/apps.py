from django.apps import AppConfig


class ComplaintsConfig(AppConfig):#Defines a configuration class for the complaints app.


    default_auto_field = 'django.db.models.BigAutoField'#pecifies the default type of primary key for models
    name = 'complaints'
#Every Django app has an apps.py file that registers the app with Django.

