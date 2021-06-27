
from django.urls import path
from .views import *

urlpatterns = [
   
    path('', registeruser),
    path('verify/<token>/' , verify_user),
    path('login/',loginuser )
   
   
]
