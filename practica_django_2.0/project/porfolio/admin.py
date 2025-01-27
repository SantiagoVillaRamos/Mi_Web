from django.contrib import admin
from .models import PorfolioForm
# Register your models here.
# class PorfolioAdmin(admin.ModelAdmin):
#     readonly_fields = ('update',)

admin.site.register(PorfolioForm)