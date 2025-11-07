from django.contrib import admin
from django.urls import path
from apps.empleado import views as empleado_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', empleado_views.login_view, name='login'),
    path('home/', empleado_views.home, name='home'),
    path('logout/', empleado_views.logout_view, name='logout'),
]
