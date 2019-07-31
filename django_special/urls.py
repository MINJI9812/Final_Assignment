
from django.contrib import admin
from django.urls import path   ,    include
import first_app.views
import second_app.views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', first_app.views.home, name='home'),
    path('blog/', include('first_app.urls') ),
    path('portfolio/', include('second_app.urls') ),

    path('account/', include('third_app.urls') ),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
