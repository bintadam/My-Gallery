from django.urls import path
from . import views
from os import name
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    path('',views.welcome,name ='welcome'),
    path('pictures/',views.pictures,name='pictures'),
    path('search/', views.search_results, name='search_results'),
    path('picture/<int:image_id>/',views.picture,name='imageid'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)