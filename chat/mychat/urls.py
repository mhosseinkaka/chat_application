from django.urls import path
from mychat.views import Main

urlpatterns = [
    path('', Main.as_view()),
]