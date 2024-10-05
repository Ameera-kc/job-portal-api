from django.urls import path, include
from .views import RoleView

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('auth/role/', RoleView.as_view(), name='user-role'),
]
