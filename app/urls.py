from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name='todo'),
    path('form/', views.form, name='form'),
    path('delete/<id>', views.delete, name='delete'),
    path('update/<id>', views.update, name='update'),
    path('log_in',views.log_in,name='log_in'),
    path('sign_up',views.sign_up,name='sign_up'),
    path('log_out',views.log_out,name='log_out')
]
