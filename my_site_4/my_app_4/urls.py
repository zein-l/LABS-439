from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_records, name='display_records'),  
    path('add/', views.add_record, name='add_record'),  
    path('modify/<int:id>/', views.modify_record, name='modify_record'),  
    path('remove/<int:id>/', views.remove_record, name='remove_record'),  
    path('completion/', views.completion, name='completion'),  
]
