from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('customers/', include('customers.urls')),
                  path('product_data/', include('product.urls')),
                  path('accounts/', include('customers.urls')),
                  path('social_auth', include('social_django.urls', namespace='social')),
                  path('app/', include('app.urls')),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
