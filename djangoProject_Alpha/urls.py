"""djangoProject_Alpha URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework import routers

from app1.views import *
from files.views import *
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

router = routers.SimpleRouter()
router.register(r'', FileAPIView)
views =Views()
urlpatterns = [
    path('admin/', admin.site.urls),
    path("excel-to-excel", views.exceltoexcel_page),
    path("word-to-excel", wordtoexcel_page),
    path("excel-to-json", exceltojson_page),
    path('', index_page), # Маршрутизатор
    path('post-editor', views.post_editor), # Маршрутизатор
    path('api2/', ConvertorAPIView.as_view(),),
    path(r'api3/', include(router.urls)),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
