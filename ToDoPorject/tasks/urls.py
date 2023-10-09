from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_task/', views.create_task),
    path('update_task/', views.change_state),
    path('delete_task/', views.delete_task)
]
