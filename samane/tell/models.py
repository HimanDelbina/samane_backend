from django.db import models

# Create your models here.


class TellModel(models.Model):
    phone = models.CharField(max_length=10, verbose_name="شماره داخلی")
    title = models.CharField(max_length=30, verbose_name="نام واحد")

    class Meta:
        verbose_name = "شماره تماس "
        verbose_name_plural = " شماره تماس ها"

    def __str__(self):
        return self.title
