from django.urls import path
from .views import home,front,login, start,videocall,logout, join

urlpatterns = [
path('', home,  name='home'),
path('login/', login, name='login'),
path('start/', start, name='start' ),

path('meeting/', videocall, name='meeting'),
path('logout/', logout, name='logout'),
path('join/', join, name='join'),
]