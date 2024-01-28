from django.db import models
from asyncore import write
from django.db import models
import barcode
from barcode.writer import ImageWriter
from io import BytesIO
from django.core.files import File
import os
from django.utils.html import mark_safe
# Create your models here.



def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def news_barcode_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.pk}-{name}{ext}"
    x = f"Barcode/{final_name}"
    return x




class PmObjectModel(models.Model):
    title = models.CharField(max_length=80, verbose_name="نام")
    isbn = models.CharField(verbose_name="شناسه بارکد", max_length=13, help_text='کالا کد')
    barcode = models.ImageField(
        blank=True, null=True, upload_to=news_barcode_path, help_text='به این قسمت کاری نداشته باشید',verbose_name="عکس")
    
    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" width="200" height="100"/>'.format(self.barcode.url))

    image_tag.short_description = 'عکس بارکد'
    image_tag.allow_tags = True

    def save(self, *args, **kwargs):
        CODE_39 = barcode.get_barcode_class('code39')
        code = CODE_39(f'{self.isbn}', writer=ImageWriter(),
                       add_checksum=False)
        buffer = BytesIO()
        code.write(buffer)
        self.barcode.save(f'{self.title}.png', File(buffer), save=False)
        return super().save(*args, **kwargs)   
    
    class Meta:
        verbose_name = "دستگاه صنعتی"
        verbose_name_plural = "دستگاه های صنعتی"