from django.urls import path
from . import member_views

urlpatterns = [
    path('', member_views.main, name='main'),
    path('members/', member_views.members, name='members'),
    path('members/details/<int:id>', member_views.details, name='details'),
    path('testing/', member_views.testing, name='testing'), 
]