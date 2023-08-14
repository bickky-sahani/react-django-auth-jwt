from django.db.models.functions import Lower
from rest_framework import viewsets, serializers, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from pydantic import ValidationError as PydanticValidationError

from account.models import CustomUser
from account.domain import commands
from account.service_layer import abstracts, exceptions, handlers, views
from account.entrypoint.permissions import CustomUserPermission


class CustomUserAccountSerializer(serializers.ModelSerializer):
    tokens = serializers.SerializerMethodField()

    def get_tokens(self, email):
        user = CustomUser.objects.get(email=email)
        return {"refresh": user.tokens()["refresh"], "access": user.tokens()["access"]}

    class Meta:
        model = CustomUser
        fields = ["id", "email", "is_staff", "is_active", "date_joined", "tokens"]


class UserAccountViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserAccountSerializer
    permission_classes = []

    def get_queryset(self):
        queryset = self.queryset
        q = self.request.query_params.get("q")
        if q:
            queryset = queryset.filter(username__icontains=q)
        return queryset

    @action(detail=False, methods=["POST"])
    def register(self, request, *args, **kwargs):
        try:
            validated_data = abstracts.AddUser(**request.data)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        cmd = commands.AddUser(**validated_data.dict())
        try:
            user = handlers.register_user(cmd=cmd)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"success": "Successfully registered user"})

    @action(detail=False, methods=["POST"])
    def login(self, request, *args, **kwargs):
        try:
            validated_data = abstracts.LoginUser(**request.data)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        cmd = commands.LoginUser(**validated_data.dict())
        try:
            user = handlers.login_user(cmd=cmd)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        data = {
            "email": user.email,
            "is_active": user.is_active,
            "date_joined": user.date_joined,
            "tokens": user.tokens(),
        }
        return Response(data)

    @action(detail=False, methods=["POST"])
    def logout(self, request, *args, **kwargs):
        refresh = request.data.get("refresh")
        try:
            RefreshToken(refresh).blacklist()
        except TokenError:
            return Response({"error": "Bad Token"})
        return Response({"success": "Successfully logged out user"})

    @action(detail=False, methods=["POST"])
    def delete(self, request, *args, **kwargs):
        user_ids = request.data.get("user_ids")
        CustomUser.objects.filter(id__in=user_ids).delete()
        return Response({"success": "Successfully deleted user"})
