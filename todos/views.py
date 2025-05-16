from django.shortcuts import render
# Create your views here.
from rest_framework.response import Response

from concurrent.futures import ThreadPoolExecutor
from rest_framework.decorators import action

from rest_framework import viewsets, permissions
from .models import Todo
from .serializers import TodoSerializer

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user

class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        return self.request.user.todos.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
        
    @action(detail=False, methods=['get'], url_path='overview')
    def overview(self, request):
        user = request.user

        def get_all():
            return list(Todo.objects.filter(user=user).values())

        def get_completed():
            return Todo.objects.filter(user=user, is_completed=True).count()

        def get_incomplete():
            return Todo.objects.filter(user=user, is_completed=False).count()

        def get_last():
            last = Todo.objects.filter(user=user).order_by('-created_at').first()
            return last.title if last else None

        with ThreadPoolExecutor() as executor:
            future_all = executor.submit(get_all)
            future_completed = executor.submit(get_completed)
            future_incomplete = executor.submit(get_incomplete)
            future_last = executor.submit(get_last)

            todos = future_all.result()
            completed = future_completed.result()
            incomplete = future_incomplete.result()
            last_title = future_last.result()

        return Response({
            "todos": todos,
            "stats": {
                "completed": completed,
                "incomplete": incomplete,
                "last_todo_title": last_title
            }
        })