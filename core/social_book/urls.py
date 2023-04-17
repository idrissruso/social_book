from django.urls import path
from social_book import views

urlpatterns = [
    path("", views.home ,name = "home")
]
