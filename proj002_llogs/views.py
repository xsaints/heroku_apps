from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Topic, Entry
from .forms import TopicForm, EntryForm


# Create your views here.
def index(request):
  ''' default main page '''
  return render(request, 'proj002_llogs/index.html')
  
  
def topics(request):
  ''' show all topics '''
  topics= Topic.objects.order_by('date_added')
  context= {'topics': topics}
  return render(request, 'proj002_llogs/topics.html', context)
  
  
def topic(request, topic_id):
  ''' show a particular topic '''
  topic= Topic.objects.get(id= topic_id)
  entries= topic.entry_set.order_by('-date_added')
  context= {'topic': topic, 'entries': entries}
  return render(request, 'proj002_llogs/topic.html', context)  
  
  
def new_topic(request):
  ''' add a new topic '''
  if request.method != 'POST':
    form= TopicForm()
  else:
    form= TopicForm(request.POST)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect(reverse('proj002_llogs:topics'))
  
  context= {'form': form}
  return render(request, 'proj002_llogs/new_topic.html', context)


def new_entry(request, topic_id):
  '''add a new entry for a particular topic'''
  topic= Topic.objects.get(id= topic_id)

  if request.method != 'POST':
    form= EntryForm()
  else:
    form= EntryForm(data= request.POST)
    if form.is_valid():
      new_entry= form.save(commit= False)
      new_entry.topic= topic
      new_entry.save()
      return HttpResponseRedirect(reverse('proj002_llogs:topic', args=[topic_id]))
  
  context= {'topic': topic, 'form': form}
  return render(request, 'proj002_llogs/new_entry.html', context)
  
  
def edit_entry(request, entry_id):
  ''' edit an existing entry'''
  entry= Entry.objects.get(id= entry_id)
  topic= entry.topic
  
  if request.method != 'POST':
    form= EntryForm(instance= entry)
  else:
    form= EntryForm(instance= entry, data= request.POST)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect(reverse('proj002_llogs:topic', args= [topic.id]))
      
  context= {'entry': entry, 'topic': topic, 'form': form}
  return render(request, 'proj002_llogs/edit_entry.html', context)
  