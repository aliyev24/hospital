from django.urls import path
from rest_framework_simplejwt.views import (TokenRefreshView,)

from . import views


urlpatterns = [
    path('api/token/',
         views.MyTokenObtainPairView.as_view(),
         name='token_obtain_pair'
         ),
    path('api/token/refresh/',
         TokenRefreshView.as_view(),
         name='token_refresh'
         ),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("login/", views.LoginView.as_view(), name="login"),
]
