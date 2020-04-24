from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('user', views.UserView)
router.register('organization', views.OrganizationView)
router.register('account', views.AccountView)

urlpatterns = [
    path('', include(router.urls))
]