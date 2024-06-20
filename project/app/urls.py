from django.urls import path
from .views import *

urlpatterns = [
    path("all/", TaskView.as_view()),
    path("products/", ProductView.as_view()),
]