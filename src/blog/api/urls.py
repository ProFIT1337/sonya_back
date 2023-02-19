from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import BlogPostApiView

blogpost_router = SimpleRouter()
blogpost_router.register(r'', BlogPostApiView)

urlpatterns = [
    path('posts/', include(blogpost_router.urls)),
]
