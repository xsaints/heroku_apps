from django.conf.urls import url
from django.contrib.auth.views import login

from . import views

urlpatterns= [
  # hello
  url(r'^hello/$', views.hello, name= 'hello'),
  
  # login page
  url(r'^login/$', login, {'template_name': 'proj002_users/login.html'}, name='login'),

  url(r'', views.logout_view, name= 'logout'),
  
  # registration page
  #url(r'^register/$', views.hello2, name= 'register'),  
]