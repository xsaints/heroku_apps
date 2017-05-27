from django.shortcuts import render

from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm


def logout_view(request):
  '''logout the user'''
  logout(request)
  return HttpResponseRedirect(reverse('proj002_llogs:index'))
  
def hello(request):
  '''
  #return HttpResponse('hello world')
  if request.method != 'POST':
    form= UserCreationForm()
  else:
    form= UserCreationForm(data= request.POST)
  
  context= {'form': form, 'request': request}
  return render(request, 'proj002_users/hello.html', context)
  '''
  if request.method != 'POST':
    # display blank registration form.
    form= UserCreationForm()
  else:
    # process completed form.
    form= UserCreationForm(data= request.POST)

    if form.is_valid():
      new_user= form.save()
      #log the user in and then redirect to home page.
      authenticated_user= authenticate(username= new_user.username, password= request.POST['password1'])
      login(request, authenticated_user)
      return HttpResponseRedirect(reverse('proj002_llogs:topics'))

  context= {'form': form}
  return render(request, 'proj002_users/hello.html', context)