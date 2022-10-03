from django.urls import reverse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from .models import Dog, Work

class Home(TemplateView):
    template_name = 'home.html'
class About(TemplateView):
    template_name = 'about.html'
    
class DogList(TemplateView):
    template_name = 'dog_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get('name')
        if name != None:
                context["dogs"] = Dog.objects.filter(name__icontains=name)
                context["header"] = f"Searching for {name}"
        else:
                context["dogs"] = Dog.objects.all()
                context["header"] = "Dogs"
        return context    
class DogCreate(CreateView):
    model = Dog
    fields = ['name', 'img', 'info', 'is_dog' ]
    template_name = 'dog_create.html'
    def get_success_url(self):
        return reverse('dog_detail', kwargs={'pk': self.object.pk})
        #success_url = "/dogs/"

class DogDetail(DetailView):
    model = Dog
    template_name = 'dog_detail.html'

class DogUpdate(UpdateView):
    model = Dog
    fields = ['name', 'img', 'info','is_dog']
    template_name = 'dog_update.html'
    def get_success_url(self):
        return reverse('dog_detail', kwargs={'pk': self.object.pk})
    #success_url = "/dogs/<int:dog.pk>/"
class DogDelete(DeleteView):
    model = Dog
    template_name = 'dog_delete_confirmation.html'
    success_url = "/dogs"

class WorkCreate(CreateView):
    def post(self, request, pk):
        title = request.POST.get('title')
        img = request.POST.get('img')
        description = request.POST.get('description')
        artist = Dog.objects.get(pk=pk)
        Work.objects.create(title=title, img=img, description=description, artist=artist)
        return redirect('dog_detail', pk=pk)