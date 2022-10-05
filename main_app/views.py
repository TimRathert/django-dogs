from django.urls import reverse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Dog, Work, Gallery

class Home(TemplateView):
    template_name = 'home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["gallerys"] = Gallery.objects.all()
        return context
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

class MyDogs(TemplateView):
    template_name = 'my_dogs.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            name = self.request.GET.get('name')
            if name != None:
                    context["dogs"] = Dog.objects.filter(name__icontains=name, user=self.request.user)
                    context["header"] = f"Searching for {name}"
            else:
                    context["dogs"] = Dog.objects.filter(user=self.request.user)
                    context["header"] = "My Dogs"
            return context
        else:
            context["header"] = "Nothing to see here"
            return context

class DogCreate(CreateView):
    model = Dog
    fields = ['name', 'img', 'info', 'is_dog' ]
    template_name = 'dog_create.html'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(DogCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('dog_detail', kwargs={'pk': self.object.pk})   

class DogDetail(DetailView):
    model = Dog
    template_name = 'dog_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['gallerys'] = Gallery.objects.all()
        return context
        

class DogUpdate(UpdateView):
    model = Dog
    fields = ['name', 'img', 'info','is_dog']
    template_name = 'dog_update.html'
    def get_success_url(self):
        return reverse('dog_detail', kwargs={'pk': self.object.pk})

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

class GalleryWorkAssoc(View):
    def get(self, request, pk, work_pk):
        assoc = request.GET.get('assoc')
        if assoc == 'remove':
            Gallery.objects.get(pk=pk).works.remove(work_pk)
        if assoc == 'add':
            Gallery.objects.get(pk=pk).works.add(work_pk)
        return redirect('home')

class Signup(View):
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("dog_list")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)
class GalleryCreate(CreateView):
    model = Gallery
    fields = ['name', 'city', 'country' ]
    template_name = 'gallery_create.html'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(GalleryCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('home')

class GalleryUpdate(UpdateView):
    model = Gallery
    fields = ['name', 'city', 'country']
    template_name = 'gallery_update.html'
    success_url = "/"
    # def get_success_url(self):
    #     return reverse('home', kwargs={'pk': self.object.pk})

class GalleryDelete(DeleteView):
    model = Gallery
    template_name = 'gallery_delete_confirmation.html'
    success_url = "/"