from django.db.models.functions import Lower
from rest_framework import viewsets, serializers, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from rest_framework.permissions import IsAuthenticated

from pydantic import ValidationError as PydanticValidationError

from account.entrypoint.route_handlers import CustomUserAccountSerializer
from account.models import CustomUser
from task.models import Task
from task.domain import commands
from task.service_layer import abstracts, exceptions, handlers, views


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "email", "is_active"]


class TaskSerializer(serializers.ModelSerializer):
    # created_by = CustomUserAccountSerializer(read_only=True)
    created_by = CustomUserSerializer(read_only=True)

    class Meta:
        model = Task
        fields = [
            "id",
            "title",
            "description",
            "created_at",
            "updated_at",
            "completed",
            "created_by",
        ]


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.filter()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = self.queryset
        q = self.request.query_params.get("title")
        if q:
            queryset = queryset.filter(title__icontains=q)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        try:
            validated_data = abstracts.AddTask(**request.data)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        cmd = commands.AddTask(**validated_data.dict())
        try:
            print("req user", request.user)
            task = handlers.create_task(cmd=cmd, user=request.user)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"success": "Successfully created a task"})

    def update(self, request, *args, **kwargs):
        try:
            print("req data", request.data)
            validated_data = abstracts.UpdateTask(**request.data)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        print("validated_data", validated_data)
        cmd = commands.UpdateTask(**validated_data.dict())
        try:
            task = handlers.update_task(cmd=cmd, user=request.user, id=kwargs.get("pk"))
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"success": "Successfully updated a task"})

    @action(detail=False, methods=["POST"])
    def delete(self, request, *args, **kwargs):
        task_ids = request.data.get("task_ids")
        Task.objects.filter(id__in=task_ids).delete()
        return Response({"success": "Successfully deleted task"})
