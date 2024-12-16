from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profile_pic')
    bio = models.CharField(default='',max_length=100)

    def __str__(self):
        return f'{self.user.username} Profile'

    @property
    def name(self):
        if self.user.username:
            return self.user.username
        return self.user.username

    @property
    def avatar(self):
        if self.image:
            return self.image.url
        return f'{settings.STATIC_URL}images/avatar.svg'

    def save(self, *args, **kwargs):
        # Your custom save logic here
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)