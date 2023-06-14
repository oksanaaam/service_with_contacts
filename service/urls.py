from django.urls import path
from .views import ContactSearchView


urlpatterns = [
    path("contact/search/", ContactSearchView.as_view(), name="contact-search"),
]

app_name = "service"
