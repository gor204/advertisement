from django.urls import path
from .views import index, top_sellers
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static


urlpatterns = [
    path('', index, name="main-page"),
    path('top-sellers/', top_sellers, name="sellers"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

