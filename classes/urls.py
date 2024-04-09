from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_classes, name='classes'),
    path('<int:class_type_id>', views.class_info, name='class_type'),
]