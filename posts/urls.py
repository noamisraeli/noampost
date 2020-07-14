from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from posts.views import PostView, AuthorView

router = routers.DefaultRouter()
router.register('posts', PostView)
router.register('authors', AuthorView)

urlpatterns = [
    path('', include(router.urls))
]
