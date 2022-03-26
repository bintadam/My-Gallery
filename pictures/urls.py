from django.urls import re_path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    re_path('^$',views.welcome,name = 'welcome'),
    re_path('^pictures/$',views.pictures,name='pictures'),
    re_path('^search/', views.search_results, name='search_results'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)