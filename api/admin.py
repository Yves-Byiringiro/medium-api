from django.contrib import admin
from api.models import *



class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Category, CategoryAdmin)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','content','created_at')
    search_fields = ('title','created_at')

admin.site.register(Article, ArticleAdmin)


