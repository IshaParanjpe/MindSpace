from django.contrib import admin

from . import models

# Register your models here.
admin.site.register(models.Therapy)
admin.site.register(models.Blog)
admin.site.register(models.Rec)
admin.site.register(models.Profile)
admin.site.register(models.Meditation)
admin.site.register(models.Journaling)