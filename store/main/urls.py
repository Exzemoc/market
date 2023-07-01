from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('users/', include('users.urls')),
                  path('', include('home.urls')),
                  path('products/', include('storage.urls')),
                  path('cart/', include('orders.urls')),
                  path('staff_orders/', include('staff_status.urls')),
                  path('api/', include('storage.urls')),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
