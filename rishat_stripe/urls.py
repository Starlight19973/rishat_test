from django.urls import path
from . import views

urlpatterns = [
    path('item/<int:id>/', views.item_view, name='item_view'),
    path('buy/<int:id>/', views.create_checkout_session, name='create_checkout_session'),
]
