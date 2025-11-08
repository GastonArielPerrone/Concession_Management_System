from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from apps.empleado import views as empleado_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', empleado_views.login_view, name='login'),
    path('home/', empleado_views.home, name='home'),
    path('empleado/register/', empleado_views.register_view, name='registerEmployed'),
    path('logout/', empleado_views.logout_view, name='logout'),
    path('vehiculos/', include('apps.vehiculo.urls')),
    path('ventas/', include('apps.venta.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
