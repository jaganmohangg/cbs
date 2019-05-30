from django.contrib import admin
from testapp.models import FBV_MODEL

# Register your models here.
class FBV_ADMIN(admin.ModelAdmin):
    list_display=['enumber','ename','esal','eaddrs','id']
admin.site.register(FBV_MODEL,FBV_ADMIN)
