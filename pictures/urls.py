from django.urls import re_path
from . import views

urlpatterns=[
    re_path('^$',views.welcome,name = 'welcome'),
    re_path('^today/$',views.pictures_of_day,name='picturesToday'),
]
