from django.urls import path
from .views import *

urlpatterns = [
    path('', login, name='login'),
    path('signup', signup, name='signup'),
    path('table', table, name='table'),
    path('add_member', add_member, name='add_member'),
    path('logout', logout, name='logout'),
    path('check', check, name='check'),
]