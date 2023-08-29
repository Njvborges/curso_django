from django.urls import path

from recipes.views import home, contacto, sobre

urlpatterns = [
    path('', home),  # Home
    path('sobre/', sobre),  # /sobre/
    path('contacto/', contacto),  # /contacto
]
