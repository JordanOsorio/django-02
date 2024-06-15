from django.urls import path
from . import views, include

urlpatterns = [
    path('index', views.index, name='index'),
    path('alumnos/',include('alumnos.urls'))

]
