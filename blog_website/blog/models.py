from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# importung pillow to resize the image
from PIL import Image
from django.urls import reverse

# This stuff is the like the biodata of a post


class Post(models.Model):
    title = models.CharField(max_length=50)
    # TextField Is Unlimited Characters Maybe
    content = models.TextField()
    # This Is For The Current Date And Time
    date = models.DateTimeField(default=timezone.now)
    # models.CASCADE means that when the author or user is deleted, delete this post too
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # This just returns the stuff we've written in it when we asks for the model object,
    # in this case it'll written the title of the post
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post-content', kwargs={'pk': self.pk})


# This is for the MY PROFILE button to display the images and stuff
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return('%s Profile' % self.user.username)
    # This stuff is to resize the image using the pillow module as it reduces the size of the image

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            img_size = (300, 300)
            img.thumbnail(img_size)
            img.save(self.image.path)


# Create your models here.
