from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path
from django.conf.urls.static import static
from django.urls.conf import include
from postin import settings

def home_view(request):
    if request.user.is_authenticated:
        return redirect('home/')
    else:
        return redirect('users/login/')

urlpatterns = [
    path('', home_view),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('', include('posts.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

