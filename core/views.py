from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from .models import Event, Booking
from .serializers import EventSerializer, BookingSerializer, RegisterSerializer, UserSerializer
from .permissions import IsOrganizerOrAdmin
from rest_framework_simplejwt.views import TokenObtainPairView

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAuthenticated(), IsOrganizerOrAdmin()]
        return [IsAuthenticated()]

class BookingViewSet(viewsets.ModelViewSet):
    serializer_class = BookingSerializer

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)