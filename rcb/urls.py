from rcb.views import *
from django.urls import path
app_name='everything'

urlpatterns=[
    path('virat/',virat,name='virat'),
    path('siraj/',siraj,name='siraj'),
]