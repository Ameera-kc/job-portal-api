from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import JobListing, JobApplication
from .serializers import JobListingSerializer, JobApplicationSerializer
from users.permissions import IsAdmin, IsEmployer, IsCandidate

class JobListingViewSet(viewsets.ModelViewSet):
    queryset = JobListing.objects.all()
    serializer_class = JobListingSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'company__name', 'location']
    ordering_fields = ['salary', 'location', 'is_active']

    def get_permissions(self):
        if self.request.user.role == 'admin':
            return [IsAdmin()]
        elif self.request.user.role == 'employer':
            if self.action in ['create', 'update', 'destroy']:
                return [IsEmployer()]
        elif self.action == 'list':
            return [IsAuthenticated()]
        return super().get_permissions()

    def get_queryset(self):
        if self.request.user.role == 'admin':
            return JobListing.objects.all()
        elif self.request.user.role == 'employer':
            return JobListing.objects.filter(company__owner=self.request.user)
        return JobListing.objects.filter(is_active=True)


class JobApplicationViewSet(viewsets.ModelViewSet):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer

    def get_permissions(self):
        if self.request.user.role == 'admin':
            return [IsAdmin()]
        elif self.request.user.role == 'employer':
            return [IsEmployer()]
        elif self.action in ['create', 'list']:
            return [IsCandidate()]
        return super().get_permissions()

    def get_queryset(self):
        if self.request.user.role == 'admin':
            return JobApplication.objects.all()
        elif self.request.user.role == 'employer':
            return JobApplication.objects.filter(job__company__owner=self.request.user)
        return JobApplication.objects.filter(candidate=self.request.user)
