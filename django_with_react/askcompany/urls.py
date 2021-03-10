"""askcompany URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

# from django.conf import global_settings  # global_settings에 우리가 만든 settings를 overwrite하는 것이기 때문에 함께 해야 함
# from askcompany import settings  # settings 참조 시 이렇게 하면 안됨
from django.conf import settings  # 따라서 이렇게 해주면 됨

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog1/', include('blog1.urls')),
    path('instagram/', include('instagram.urls')),
]

if settings.DEBUG:  # 개발 모드일 때는 DEBUG가 TRUE
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # url list를 주므로 이를 추가, 실제 요청된 이미지를 읽어서 보여주기 위해 사용

# settings.MEDIA_URL
# settings.MEDIA_ROOT
