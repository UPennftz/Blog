"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from django.urls import re_path, include, path

from blog import views
from django.contrib import admin


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet, basename='users')
router.register(r'blogs', views.BlogViewSet, basename='blogs')
router.register(r'comments', views.CommentViewSet, basename='comments')

urlpatterns = [
    # f加的引用
    path('api/blogs/', views.get_blogs),
    path('api/create-blog/', views.create_blog),

    re_path('admin/', admin.site.urls),
    path('', include(router.urls)),
    re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
