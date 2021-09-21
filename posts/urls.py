# core django
from django.urls import path

# 3rd
from rest_framework.routers import SimpleRouter

# local
from .views import UserViewSet, PostViewSet

router = SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('', PostViewSet, basename='posts')

urlpatterns = router.urls
