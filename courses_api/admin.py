from django.contrib import admin
from courses import models


# Register your models here.

@admin.register(models.Course)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created', 'slug',)
    prepopulated_fields = {'slug': ('title',), }

@admin.register(models.Review)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'course', 'rating', 'comment')

admin.site.register(models.Category)