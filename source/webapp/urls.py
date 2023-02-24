from django.urls import path

from webapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/task', views.add_task, name='add'),
    path('todo_list', views.todo_list, name='list'),
    path('inform_list/<int:pk>', views.inform_list, name='inform'),
    path('inform_list/<int:pk>/update/', views.update_view, name='todo_update'),
    path('inform_list/<int:pk>/delete/', views.confirm_delete, name='confirm_delete'),
]
