from django.shortcuts import render
from rest_framework import generics
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer


def home(request):
    return render(request, 'index.html')


class MenuView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class BookingView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer