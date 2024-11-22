from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import main, pdf1, pdf2, upload_sql, display_sql, list_databases

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name='main'),
    path('pdf1/', pdf1, name='pdf1'),
    path('pdf2/', pdf2, name='pdf2'),
    path('upload/', upload_sql, name='upload_sql'),
    path('display/', display_sql, name='display_sql'),
    path('databases/', list_databases, name='list_databases'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
