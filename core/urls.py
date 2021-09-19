from django.urls import path

from core.views import *


urlpatterns=[
        path('',home, name='home'),
        path('cadastrar', cadastrar, name='cadastrar'),
        path('update/<int:id>', update, name='update'),
        path('apagar/<int:id>', apagar, name='apagar'),
        path('listar',listar, name='listar'),


        ]
