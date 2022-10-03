from django.db import models

class Dog(models.Model):
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    info = models.TextField(max_length=500)
    is_dog = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
class Work(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=400)
    date_created = models.DateTimeField(auto_now_add=True)
    artist = models.ForeignKey(Dog, on_delete=models.CASCADE, related_name="works")

    def __str__(self):
        return self.title