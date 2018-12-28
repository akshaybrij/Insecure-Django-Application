from django.contrib import admin
from .models import InsecureModel

admin.site.register(InsecureModel)
