from rest_framework import generics
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer


class MenuView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class BookingView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer