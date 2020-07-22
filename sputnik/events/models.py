from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.

class event(models.Model):
    event_title = models.CharField('Название мероприятия', max_length=50)
    event_text = RichTextField('Текст записи', blank=True)
    image = models.ImageField(null=False, upload_to="images/", verbose_name='Изображение')
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.event_title

    class Meta:
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"


class PostsImages(models.Model):
    images = models.ImageField(upload_to="images/", blank=True)
    post = models.ForeignKey(event, related_name='PostsImages', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.post)

    class Meta:
        verbose_name = "Картинка"
        verbose_name_plural = "Картинки"
