from rest_framework import views, status, serializers
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.users.models import User


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        return RefreshToken.for_user(user)

    def validate(self, attrs):
        user = User.objects.get(email=attrs['email'])
        if not user.is_active or user.role != User.Role.ADMIN:
            raise serializers.ValidationError({'email': 'There is no user with this credentials'})

        data = super().validate(attrs)

        return data


class TokenObtainPairPatchedAdminView(TokenObtainPairView):
    permission_classes = [AllowAny]
    serializer_class = MyTokenObtainPairSerializer


class TokenObtainPairPatchedUserView(TokenObtainPairView):
    permission_classes = [AllowAny]


class UserLogoutView(views.APIView):
    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({'message': "User logged out successfully."}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as err:
            return Response({'message': 'Something went wrong, please try again.'}, status=status.HTTP_400_BAD_REQUEST)
