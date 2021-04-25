from django.contrib import admin
from BRMapp import models as mod

# Register your models here.
admin.site.register(mod.Book)
admin.site.register(mod.BRMuser)