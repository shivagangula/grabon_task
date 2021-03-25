
from django.contrib import admin
from django.urls import path
from fare_cal.views import boarding_names_ajex


from django.conf import settings
from django.conf.urls.static import static
from fare_cal.views import test
urlpatterns = [
    path('admin/', admin.site.urls),
    path('bnajex/', boarding_names_ajex, name='boarding_names_ajex'),
    path('', test),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
