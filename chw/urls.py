from django.conf.urls import url
from django.urls import path
from .views import index,household

urlpatterns = [
    path('index/',index,name='index'),
    path('household/',household,name='household')
]

