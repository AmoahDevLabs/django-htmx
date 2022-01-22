from django.urls import path
from .views import todos_list, search, add_todo, update_todo, delete_todo

urlpatterns = [
    path('', todos_list, name='todos'),
    path('add-todo/', add_todo, name='add_todo'),
    path('update/<int:pk>/', update_todo, name='update_todo'),
    path('delete/<int:pk>/', delete_todo, name='delete_todo'),
    path('search/', search, name='search'),

]
