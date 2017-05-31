from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required


from .models import Topic, Entry
from .forms import TopicForm, EntryForm


# Create your views here.
def index(request):
  ''' default main page '''
  return render(request, 'proj002_llogs/index.html')
  
  
@login_required  
def topics(request):
  ''' show all topics '''
  #topics= Topic.objects.order_by('date_added')
  topics= Topic.objects.filter(owner= request.user).order_by('date_added')
  context= {'topics': topics}
  return render(request, 'proj002_llogs/topics.html', context)
  
  
@login_required  
def topic(request, topic_id):
  ''' show a particular topic '''
  #topic= Topic.objects.get(id= topic_id)
  topic= get_object_or_404(Topic, id= topic_id)
  if topic.owner != request.user:
    raise Http404
  entries= topic.entry_set.order_by('-date_added')
  context= {'topic': topic, 'entries': entries}
  return render(request, 'proj002_llogs/topic.html', context)  
  
  
@login_required  
def new_topic(request):
  ''' add a new topic '''
  if request.method != 'POST':
    form= TopicForm()
  else:
    form= TopicForm(request.POST)
    if form.is_valid():
      new_topic= form.save(commit= False)
      new_topic.owner= request.user
      form.save()
      return HttpResponseRedirect(reverse('proj002_llogs:topics'))
  
  context= {'form': form}
  return render(request, 'proj002_llogs/new_topic.html', context)

  
@login_required
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
  
  
@login_required  
def edit_entry(request, entry_id):
  ''' edit an existing entry'''
  entry= Entry.objects.get(id= entry_id)
  topic= entry.topic
  
  if topic.owner != request.user:
    raise Http404
    
  if request.method != 'POST':
    form= EntryForm(instance= entry)
  else:
    form= EntryForm(instance= entry, data= request.POST)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect(reverse('proj002_llogs:topic', args= [topic.id]))
      
  context= {'entry': entry, 'topic': topic, 'form': form}
  return render(request, 'proj002_llogs/edit_entry.html', context)
  