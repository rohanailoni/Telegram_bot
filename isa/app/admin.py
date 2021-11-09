from django.contrib import admin

# Register your models here.
from app.models import user,Document


admin.site.register(user)
admin.site.register(Document)
