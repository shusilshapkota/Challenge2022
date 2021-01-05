from django.db import models
from django.utils.translation import gettext_lazy as _
from datetime import datetime
from django.contrib.auth.models import User


def upload_to(instance, filename):
    file_extension = str(datetime.now())
    return 'posts/{filename}'.format(filename=file_extension+"_"+filename)


# Create your models here.

# UserImages model that stores images for the logged in user
class UserImages(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user", default=None)
    uploaded_date = models.DateTimeField(default=datetime.now, blank=True)
    private = models.BooleanField(default=False)
    image = models.ImageField(_("Image"), upload_to=upload_to, default='post/default.jpg')

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ['id']
