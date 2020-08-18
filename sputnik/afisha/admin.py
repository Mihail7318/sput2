from django.contrib import admin
from .models import afisha
class AfishaAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'time', 'price', 'date_pub')
admin.site.register(afisha, AfishaAdmin)
# Register your models here.
