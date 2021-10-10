from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_images')
    biography = models.TextField(null=True)

    followers = models.ManyToManyField(User, related_name="followers_user")
    following = models.ManyToManyField(User, related_name="following_user")

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            img.resize((300, 300), Image.ANTIALIAS)
            img.save(self.image.path, optimize=True, quality=95)