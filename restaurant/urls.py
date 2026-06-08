from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import MenuView, BookingView, home

urlpatterns = [
    path('', home),

    path('menu/', MenuView.as_view()),
    path('bookings/', BookingView.as_view()),
    path('api-token-auth/', obtain_auth_token),
]