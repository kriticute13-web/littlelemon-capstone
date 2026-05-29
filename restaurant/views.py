from rest_framework import generics
from .models import Booking
from .serializers import BookingSerializer

class BookingView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer