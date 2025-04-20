from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('greet/<str:name>/', views.greet, name='greet'),
    path('books/', views.book_list, name='books'),
]
