from django.contrib import admin
from django.urls import path, include
from chat_main.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('', include('chat_main.urls')),
    path("accounts/profile/", profile, name='profile'),
    path('<int:pk>/edit/', ProfileUpdate.as_view()),
    path('<int:pk>/new/', ProfileCreate.as_view()),
    path('<int:pk>/profiledetail/', profiledetailview, name='profiledetail'),
    path("accounts/", include("allauth.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
