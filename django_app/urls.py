from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'django_app/persons', views.PersonView)

app_name = 'django_app'
