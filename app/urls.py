from django.urls import path
from .views import FieldsListView, FieldDetailView, FieldCreateView

urlpatterns = [
    path('post/new/', FieldCreateView.as_view(), name='field_new'), 
    path('', FieldsListView.as_view(), name='home'),
    path('field/<int:pk>/', FieldDetailView.as_view(), name='field_detail'), 
]