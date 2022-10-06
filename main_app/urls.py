from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('dogs/', views.DogList.as_view(), name="dogs"),
    path('dogs/mine', views.MyDogs.as_view(), name="my_dogs"),
    path('dogs/new', views.DogCreate.as_view(), name = "dog_create"),
    path('dogs/<int:pk>/', views.DogDetail.as_view(), name="dog_detail"),
    path('dogs/<int:pk>/update', views.DogUpdate.as_view(), name="dog_update"),
    path('dogs/<int:pk>/delete', views.DogDelete.as_view(), name="dog_delete"),
    path('dogs/<int:pk>/works/new', views.WorkCreate.as_view(), name="work_create"),
    path('accounts/signup/', views.Signup.as_view(), name="signup"),
    path('galleries/', views.Galleries.as_view(), name = "galleries_home"),
    path('galleries/<int:pk>/works/<int:work_pk>/', views.GalleryWorkAssoc.as_view(), name = "gallery_work_assoc"),
    path('galleries/new', views.GalleryCreate.as_view(), name = "gallery_create"),
    path('galleries/<int:pk>/update', views.GalleryUpdate.as_view(), name="gallery_update"),
    path('galleries/<int:pk>/delete', views.GalleryDelete.as_view(), name="gallery_delete"),
]   