
from django.urls import path,include
from apps.views import main_page,region_page

urlpatterns = [
    path('',main_page,name='main_page'),
    path('region/<int:pk>/',region_page,name='region'),
]