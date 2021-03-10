from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Post

# Register your models here.
# admin.site.register(Post)  # 첫 번째 등록 방법


# class PostAdmin(admin.ModelAdmin):  # 두 번째 등록 방법
#     pass
#
#
# admin.site.register(Post, PostAdmin)


@admin.register(Post)  # 세 번째 등록 방법 - Wrapping
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'photo_tag', 'message', 'message_length', 'is_public', 'created_at', 'updated_at']
    list_display_links = ['message']
    list_filter = ['created_at', 'is_public']
    search_fields = ['message']

    def photo_tag(self, post):
        if post.photo:
            return mark_safe(f'<img src="{post.photo.url}" style="width: 72px" />')
        return None

    def message_length(self, post):  # admin이 호출하는 post 객체
        return len(post.message)
    message_length.short_description = "메세지 글자수"
