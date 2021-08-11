from django.contrib import admin
from caregories.models import Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title","published"]
# Register your models here.
