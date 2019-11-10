from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.post_list, name='post_list'),
]