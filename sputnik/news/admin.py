from django.contrib import admin
from django.contrib import admin
from .models import article, covid

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'date_a')
admin.site.register(article, ArticleAdmin)
admin.site.register(covid)
# Register your models here.

