from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app1.urls')),
    path('about/', include('app2.urls')),
    path('raspberry/', include('raspberry.urls')),
]
