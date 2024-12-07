from django.urls import path
from . import views

app_name = "labyrinth"
urlpatterns = [
    path('', views.maze_view, name='labyrinth'),
]
