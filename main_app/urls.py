from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('dogs/', views.DogList.as_view(), name="dogs"),
    path('dogs/new', views.DogCreate.as_view(), name = "dog_create"),
    path('dogs/<int:pk>/', views.DogDetail.as_view(), name="dog_detail"),
    path('dogs/<int:pk>/update', views.DogUpdate.as_view(), name="dog_update"),
    path('dogs/<int:pk>/delete', views.DogDelete.as_view(), name="dog_delete"),
    path('dogs/<int:pk>/works/new', views.WorkCreate.as_view(), name="work_create"),
    path('galleries/<int:pk>/works/<int:work_pk>/', views.GalleryWorkAssoc.as_view(), name = "gallery_work_assoc")
]   