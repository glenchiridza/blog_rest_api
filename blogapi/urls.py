from django.contrib import admin
from django.urls import path
from django.conf.urls import include

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rest-auth', include("rest_auth.urls")),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('api/token', obtain_auth_token, name="obtain-token")
]
