from django.urls import path

from .views import admin, user


urlpatterns = [
    path('admin/', admin),
    path('user/', user)
]