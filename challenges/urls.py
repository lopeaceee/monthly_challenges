from django.urls import path
from . import views

urlpatterns = [
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge, name="month-challenge"),
]

# if a request reached "/january", then execute the 
# index view function
# we want to configure the URL 
