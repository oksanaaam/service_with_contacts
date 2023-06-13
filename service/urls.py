from django.urls import path
from .views import ContactSearchView

urlpatterns = [
    path("api/contact/search/", ContactSearchView.as_view(), name="contact_search"),
]

app_name = "service"
