from django.urls import path
from . import views

urlpatterns = [
    path('registrations/',views.showformdata),
]
