
import os
from io import BytesIO
from PIL import Image
from django.core.files.base import ContentFile
from django.db import models
from ckeditor.fields import RichTextField

class SiteSettings(models.Model):
    site_title=models.CharField(max_length=200,default="Langlang's Art Gallery")
    footer_text=models.CharField(max_length=255,default="© 2024 All rights reserved.")

class Section(models.Model):
    slug=models.SlugField(unique=True)
    nav_label=models.CharField(max_length=50)
    title=models.CharField(max_length=200)
    body=RichTextField(blank=True)
    order=models.PositiveIntegerField(default=0)
    is_active=models.BooleanField(default=True)
    class Meta: ordering=["order"]

class GalleryImage(models.Model):
    section=models.ForeignKey(Section,on_delete=models.CASCADE,related_name="images",
    limit_choices_to={"slug":"gallery"})
    image=models.ImageField(upload_to="gallery/originals/")
    thumb=models.ImageField(upload_to="gallery/thumbs/",blank=True,null=True,editable=False)
    title=models.CharField(max_length=200,blank=True)
    caption=models.TextField(blank=True)
    order=models.PositiveIntegerField(default=0)
    is_active=models.BooleanField(default=True)
    THUMB_MAX_SIZE=(900,900)
    class Meta: ordering=["order"]
    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        if self.image and not self.thumb:
            img=Image.open(self.image).convert("RGB")
            img.thumbnail(self.THUMB_MAX_SIZE)
            io=BytesIO()
            img.save(io,format="JPEG",quality=85)
            name=os.path.splitext(os.path.basename(self.image.name))[0]+"_thumb.jpg"
            self.thumb.save(name,ContentFile(io.getvalue()),save=False)
            super().save(update_fields=["thumb"])
