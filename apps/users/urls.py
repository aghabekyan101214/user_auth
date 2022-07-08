from django.urls import path
from apps.users import views
from apps.core.auth import TokenObtainPairPatchedUserView, TokenRefreshView

app_name = "users"

urlpatterns = [
    path('auth/', TokenObtainPairPatchedUserView.as_view(), name='auth'),
    path('refresh-token/', TokenRefreshView.as_view(), name='auth'),
]
