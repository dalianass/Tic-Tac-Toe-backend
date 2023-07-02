from django.urls import path
from . import views

# mora se ovako nazvati
urlpatterns = [
    path("minii/", views.minimax),
    path("geet/<board>", views.getData),
    path("tabla/", views.getBoard),
]