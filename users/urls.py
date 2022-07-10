from django.urls import path, include

urlpatterns = [
    # Include default auth urls.
    path('', include('django.contrib.auth.urls')),
]