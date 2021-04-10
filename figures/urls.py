from django.urls import path
from . import views

app_name = 'figures'

urlpatterns = [
    path('',views.figure_list,name='figures'),
    path('info/<int:id>', views.figure_detail, name='detail'),
    path('create/',views.figure_create,name='create'),
    path('edit/<int:pk>',views.figure_edit,name='edit'),
    path('delete/<int:pk>',views.figure_delete,name='delete'),

]