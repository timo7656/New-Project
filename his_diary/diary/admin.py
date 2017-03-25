from django.contrib import admin
from .models import Article, Comment
# Register your models here.

#admin 항목들 추가!!
@admin.register(Article, Comment)
class DiaryAdmin(admin.ModelAdmin):
    pass
