from django.urls import path
from . import  views
from django.conf.urls import include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hello_viewset', views.HelloViewSet, basename='hello_viewset')
router.register('profile', views.UserProfileViewSet, basename='profile')

urlpatterns = [
    path('hello_view/', views.HelloApiView.as_view(), name='hello_view'),
    path(r'', include(router.urls)),
]
