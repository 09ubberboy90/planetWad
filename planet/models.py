import logging
import os
import PIL
from django.db import models
from django.contrib.auth.models import UserManager, User
from django.contrib.auth.validators import ASCIIUsernameValidator
from WadThePlanet import settings
from django.contrib.auth.models import User


# ======================== Utilities ===========================================

logger = logging.getLogger(__name__)

# ======================== Models ==============================================

# Create your models here.*

class PlanetUser(models.Model):
    user = models.OneToOneField(User)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255)
    identifier = models.CharField(max_length=40, unique=True)
    avatar = models.ImageField(
        upload_to='profile_images', blank=True, null=True)

    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username


class Planet(models.Model):
    # The size of the textures to save (in pixels, should be power-of-two)
    TEXTURE_SIZE = 2048

    # An unique numeric id for each planet
    id = models.AutoField(null=False, primary_key=True)
    # The name of the planet
    name = models.CharField(null=False, max_length=50)
    # The planet's texture (as painted by the user).
    texture = models.ImageField(null=False, upload_to='planets')

    def save(self, *args, **kwargs):
        # Overridden save() method that resizes the uploaded `texture` if required
        super().save(*args, **kwargs)
        with PIL.Image.open(self.texture.path) as pil_img:
            width, height = pil_img.size
            if width != self.TEXTURE_SIZE or height != self.TEXTURE_SIZE:
                # Rescale image to correct size and save
                logger.debug(f'Planet{self.id}: Image has wrong size {width}x{height},'
                             f'resizing it to {self.TEXTURE_SIZE}x{self.TEXTURE_SIZE}')
                pil_img.resize((self.TEXTURE_SIZE, self.TEXTURE_SIZE), resample=PIL.Image.BICUBIC)
                pil_img.save(self.texture.path, quality=90, optimize=True)

    def __str__(self) -> str:
        return self.name
