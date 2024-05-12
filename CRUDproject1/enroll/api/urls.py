from django.urls import path,include
from enroll.api import views
from rest_framework.routers import DefaultRouter

# Creating Router Object
router = DefaultRouter()
router.register('userapi', views.UserViewSet, basename='user')

urlpatterns = [
	path('', include(router.urls)),
]