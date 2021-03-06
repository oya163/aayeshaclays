from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('users', views.UserViewSet, basename="UserModel")

urlpatterns = [
    path('', include(router.urls)),
    path('users/<slug:username>', views.MyAccount.as_view()),
]