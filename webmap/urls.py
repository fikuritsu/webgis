#this is the python code that will store the urls of the views. The views is the html page render

from django.urls import path
from . import views
# from .views import index, river

urlpatterns = [
    path('', views.index, name = 'index' ),
    path('riverData', views.river, name='riverData'),
    # path('home', views.home, name='home'),
    path('testing', views.testing, name='testing'),
    path('markerData', views.marker, name='markerData'),
    path('radius', views.radius, name='radius'),
    path('home', views.Home.as_view(), name='Home'),
    path('loading', views.loading, name='loading'),
]

