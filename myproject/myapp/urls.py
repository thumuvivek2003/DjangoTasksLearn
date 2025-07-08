from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_view),
    path('hello2/', views.hello_vivek),
]
