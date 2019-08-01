from django.contrib import admin

from posts.models import Post, Comment


# Django model admin
# https://docs.djangoproject.com/en/2.2/ref/contrib/admin

class CommentInline(admin.StackedInline):
    model = Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'author', 'created_at', )
    list_filter = ('author', 'created_at', )
    inlines = [CommentInline]
    search_fields = ('author__username', 'description', )


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)


# Custom admin header
admin.site.site_header = "Djangram"
admin.site.index_title = "Admin Djangram"
