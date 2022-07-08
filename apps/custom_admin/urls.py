from django.urls import path
from apps.core.auth import TokenObtainPairPatchedAdminView, TokenRefreshView
from apps.custom_admin.views import A

app_name = "custom_admin"

urlpatterns = [
    path('auth/', TokenObtainPairPatchedAdminView.as_view(), name='auth'),
    path('refresh-token/', TokenRefreshView.as_view(), name='refresh_token'),

    path('a/', A.as_view(), name='a')
]
