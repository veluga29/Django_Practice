from django.contrib import admin
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
    pass
