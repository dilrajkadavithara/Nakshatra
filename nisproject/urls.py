from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('nisapp.urls')),  # Include your app's URLs under the 'api/' prefix
]