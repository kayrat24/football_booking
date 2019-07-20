from django.urls import path
from .views import *

urlpatterns = [
    path('post/new/', FieldCreateView.as_view(), name='field_new'), 
    path('', post_list, name='posts_list_url'),
    path('list/',field_list, name="field_list"),
    path('field/<int:pk>/', FieldDetailView.as_view(), name='field_detail'), 
]