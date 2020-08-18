from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class afisha(models.Model):
    title = models.CharField('Название мероприятия', max_length=50)
    description = RichTextField('Текст записи', blank=True)
    image = models.ImageField(null=False, upload_to="images/", verbose_name='Изображение')
    date = models.DateField()
    time = models.CharField('Время показа', max_length=20)
    price = models.IntegerField()
    date_pub = models.DateField(auto_now_add=True)



    class Meta:
        verbose_name = "Афиша"
        verbose_name_plural = "Афиша"