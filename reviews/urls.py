from django.urls import path
from . import views

urlpatterns = [
    # int: specifies the product id must be an integer
    path('add/', views.add_review, name='add_review'),
    path('edit/<int:product_id>/', views.edit_review, name='edit_review'),
    path('delete/<int:product_id>/', views.delete_review, name='delete_review'),
]
