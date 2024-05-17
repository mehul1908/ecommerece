from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Complaint)
admin.site.register(models.Product)
admin.site.register(models.ProductCategory)
admin.site.register(models.UserMaster)
admin.site.register(models.UserProfile)
admin.site.register(models.Order)