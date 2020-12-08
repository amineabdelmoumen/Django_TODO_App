
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Adminpage, name="home" ),
    path('update/<str:pk>/',views.UpdateTodo,name="update_todo"),
    path('delete/<str:pk>/',views.DeleteTodo,name="delete_todo")
    
]