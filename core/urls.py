from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventViewSet, BookingViewSet, RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register('events', EventViewSet, basename='event')
router.register('bookings', BookingViewSet, basename='booking')

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('', include(router.urls))
]