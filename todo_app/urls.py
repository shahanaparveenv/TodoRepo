from django.urls import path

from todo_app import views

urlpatterns = [
    # path('',views.index,name='index'),
    path('todo',views.todo,name='todo'),
    path('todo_list',views.todo_list, name='todo_list'),
    path('', views.index, name='index'),
    path('dashboard2', views.dashboard2, name='dashboard2'),
    path('hello',views.hello,name='hello')

]