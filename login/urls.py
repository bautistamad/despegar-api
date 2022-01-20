from django.contrib import admin
from django.urls import path, include

from .views import LoginView, RegisterView

urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    
    #path('api/login/', include('login.urls'))
]
