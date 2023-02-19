from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import RoomApiView, CategoryApiView

room_router = SimpleRouter()
room_router.register(r'', RoomApiView)

categories_router = SimpleRouter()
categories_router.register(r'', CategoryApiView)

urlpatterns = [
    path('rooms/', include(room_router.urls)),
    path('categories/', include(categories_router.urls)),
]