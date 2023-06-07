from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    updated_at = models.DateTimeField(auto_now=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    liked_pins = models.ManyToManyField('Pin', related_name='liked_users')


class Pin(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='pins/', null=True, blank=True)
    likes = models.IntegerField(default=0)

    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    # Метод для збільшення кількості лайків
    def increase_likes(self):
        self.likes += 1
        self.save()

    # Метод для зменшення кількості лайків
    def decrease_likes(self):
        self.likes -= 1
        self.save()
