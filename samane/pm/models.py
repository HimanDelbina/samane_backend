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

class DeviceEngineModel(models.Model):
    title = models.CharField(max_length=100 , verbose_name="نام دستگاه یا موتور" )
    
    class Meta:
        verbose_name = "دستگاه و موتور"
        verbose_name_plural = "دستگاه ها و موتور ها"
        
    def __str__(self):
        return self.title

class UnitModel(models.Model):
    title = models.CharField(max_length=50, verbose_name="نام واحد")
    
    class Meta:
        verbose_name = "واحد"
        verbose_name_plural = "واحد ها"
        
    def __str__(self):
        return self.title    
    
    
class PmObjectModel(models.Model):
    device = models.ForeignKey(DeviceEngineModel, verbose_name="دستگاه", on_delete=models.CASCADE)
    unit = models.ForeignKey(UnitModel, verbose_name="واحد استقرار", on_delete=models.CASCADE)
    isbn = models.CharField(verbose_name="شناسه بارکد", max_length=13, help_text='کالا کد')
    barcode = models.ImageField(
        blank=True, null=True, upload_to=news_barcode_path, help_text='به این قسمت کاری نداشته باشید',verbose_name="عکس")
    location = models.CharField(max_length=50,verbose_name="محل استقرار")
    country_maker = models.CharField(max_length=50, verbose_name="کشور سازنده" , null=True, blank=True)
    company_maker = models.CharField(max_length=50, verbose_name="شرکت سازنده" , null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True) 
    
    def __str__(self):
        return self.location

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
        self.barcode.save(f'{self.device.title}.png', File(buffer), save=False)
        return super().save(*args, **kwargs)   
    
    class Meta:
        verbose_name = "دستگاه صنعتی"
        verbose_name_plural = "دستگاه های صنعتی"