from django.urls import path
from Archive import views

urlpatterns = [
    path('', views.home, name='Archive_home'),
    path('create', views.create_item, name='Archive_create'),
]

