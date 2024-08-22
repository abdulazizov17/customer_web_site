from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.views.generic import detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('customers/', include('customers.urls')),
    path('product/',include('product.urls')),
    path('accounts/', include('product.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
