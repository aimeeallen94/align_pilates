from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_classes, name='classes'),
    path('<int:class_type_id>/', views.class_info, name='class_type'),
    path('add/', views.add_class, name='add_class'),
    path('edit/<int:class_type_id>/', views.edit_class, name='edit_class'),
    path('delete/<int:class_type_id>/', views.delete_class,
         name='delete_class'),
]
