from django.urls import path, include
from django.conf.urls.static import static
from crypto_site import settings
from . import views

urlpatterns = [
    path('', views.functions_index, name='functions_index'),
    path('<int:isDigitalSig>/<int:isKeys>/<int:isHashing>/<int:isWatermark>/', views.functions_index, name='functions_index')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)