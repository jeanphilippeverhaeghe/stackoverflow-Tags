from django.urls import path

from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.saisie_question, name='saisie_question'),
]
