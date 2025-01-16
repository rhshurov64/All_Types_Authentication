from django.urls import path, include
from . import views
from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register(r"users", views.UserAPI)

urlpatterns = [
    path("login/", views.TwoFactorLoginApi.as_view()),
    path("", include(router.urls)),
]
