from rest_framework.routers import DefaultRouter
from .views import JobListingViewSet, JobApplicationViewSet

router = DefaultRouter()
router.register(r'jobs', JobListingViewSet, basename='jobs')
router.register(r'applications', JobApplicationViewSet, basename='applications')

urlpatterns = router.urls
