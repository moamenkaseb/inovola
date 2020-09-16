from django.contrib import admin
from .models import machine , machine_code , pods , pods_code
# Register your models here.
admin.site.register(machine)
admin.site.register(machine_code)
admin.site.register(pods)
admin.site.register(pods_code)
