from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, filters
from .models import Job
from .serializers import JobSerializer
from accounts.permissions import IsAdminUser
from rest_framework.permissions import BasePermission

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all().order_by('-posted_at')
    serializer_class = JobSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['location', 'category', 'job_type']

    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAuthenticated(), IsAdmin()]
        return [IsAuthenticated(), IsAdminUser()]

class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'admin'
