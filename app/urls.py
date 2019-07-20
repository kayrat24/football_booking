from django.urls import path
from .views import *

urlpatterns = [
    path('post/new/', FieldCreateView.as_view(), name='field_new'), 
    path('', post_list, name='posts_list_url'),
    path('field/<int:pk>/', FieldDetailView.as_view(), name='field_detail'), 
]