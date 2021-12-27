from django.urls import path, include
from . import apiviews


urlpatterns = [
    path('register/', apiviews.Register.as_view()),
    path('registerconfirm/', apiviews.RegisterConfirm.as_view()),
    path('profile/', apiviews.Profile.as_view()),
    path('withdraw/', apiviews.Withdraw.as_view()),
    path('charge/', apiviews.ChargeAccount.as_view()),
    path('stream/', apiviews.StreamURL.as_view()),
    path('player/', apiviews.Player.as_view()),
    path('roles/', apiviews.Roles.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]