#define url patterns for proj002_llogs.

from django.conf.urls import url

from . import views

urlpatterns= [
  #homepage
  url(r'^$', views.index, name= 'index'),

  # Show all topics.  
  url(r'^topics/$', views.topics, name= 'topics'),
  
  # show a particular topic 
  url(r'^topic/(?P<topic_id>\d+)/$', views.topic, name= 'topic'),
  
  # add a new topic
  url(r'^new_topic/$', views.new_topic, name= 'new_topic'),
  
  # add a new entry
  url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name= 'new_entry'),
  
  # edit an entry
  url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name= 'edit_entry'),
  
  
]