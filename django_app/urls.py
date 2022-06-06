from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'django_app/persons', views.PersonView)

app_name = 'django_app'
# urlpatterns = [
    # path('', views.IndexView.as_view(), name='index'),
    # path('persons/', views.ListView.as_view(), name='persons'),
    # path('person/<pk>/', views.DetailView.as_view(), name='person_details'),
# ]
