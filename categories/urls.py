from django.urls import path
from . import views

app_name='categories'

urlpatterns = [
  path('', views.categories, name='categories'),
  path('add/', views.add_category, name='add_category'),
  path('edit/<int:id>/', views.edit_category, name='edit_category'),
  path('delete/<int:id>/', views.delete_category, name='delete_category'),
]