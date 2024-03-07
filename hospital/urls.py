from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

admin.site.site_header = 'Админ панель онлайн-больницы'
admin.site.site_title = 'Моя онлайн-больница'

# 9 Урок практика
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('backend.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

]
