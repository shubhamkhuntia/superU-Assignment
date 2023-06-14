from django.urls import path
from home.views import user, login, RegisterAPI, LoginAPI


urlpatterns = [
    path('user/', user),
    path('login/', LoginAPI.as_view()),
    path('register/', RegisterAPI.as_view())
]
