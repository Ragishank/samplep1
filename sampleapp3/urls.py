from django.urls import path
from . import views
urlpatterns=[
    path('home',views.fnHome),
    path('login',views.fnLogin)
]