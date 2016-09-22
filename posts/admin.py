from django.contrib import admin

from posts.models import Post, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)
    search_fields = ('name', 'description',)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'owner', 'created_at',)
    list_filter = ('category', 'owner',)
    search_fields = ('title', 'description', 'category', 'owner',)


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
