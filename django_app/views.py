# from django.http import HttpResponse, Http404
# from django.shortcuts import render, get_object_or_404
from .models import Person
# from django.template import loader
# from django.views import generic
from rest_framework import viewsets
from .serializers import PersonSerializer


# class IndexView(generic.View):
#
#     def get(self, request, *args, **kwargs):
#         return HttpResponse('Welcome to django_app')
#
#
# class ListView(generic.ListView):
#     template_name = 'django_app/list.html'
#     context_object_name = 'persons'
#
#     def get_queryset(self):
#         return Person.objects.order_by('first_name')
#
#
# class DetailView(generic.DetailView):
#     model = Person
#     template_name = 'django_app/person_details.html'


class PersonView(viewsets.ModelViewSet):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()
