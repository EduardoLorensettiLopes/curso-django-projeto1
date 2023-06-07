from django.urls import path
from recipes.views import contact, home, about

urlpatterns = [
    path('', home),  # Home
    path('about/', about),  # /sobre/
    path('contact/', contact),  # /contato/
]