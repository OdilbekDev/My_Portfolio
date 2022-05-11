from django.contrib import admin
from django.urls import path, include
from django.conf import Settings, settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main1.urls'))
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)