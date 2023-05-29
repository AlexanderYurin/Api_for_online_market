from django.urls import path
from .views import *

urlpatterns = [
    path('registration/', RegistrationUser.as_view(), name='registration'),
    path('login/', LoginUser.as_view(), name='login'),
    path('profile/', ProfileInfo.as_view(), name='profile'),
    path('logout/', logout_user, name='logout'),
]
