# from . import views
from .views import home
from django.urls import path,include

urlpatterns = [
    path('', home, name='home'),
]