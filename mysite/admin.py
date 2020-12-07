from django.contrib import admin

# Register your models here.
from mysite import models
admin.site.register(models.Categories)
admin.site.register(models.Tag)
admin.site.register(models.Members)
admin.site.register(models.Post)

