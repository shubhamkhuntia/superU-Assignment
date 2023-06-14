from django.urls import path
from home.views import user, login


urlpatterns = [
    path('user/', user),
    path('login/', login)
]
