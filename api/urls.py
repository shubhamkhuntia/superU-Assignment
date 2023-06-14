from django.urls import path
from home.views import user, login, RegisterAPI, LoginAPI


urlpatterns = [
    path('user/', user, name='user'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('register/', RegisterAPI.as_view())
]
