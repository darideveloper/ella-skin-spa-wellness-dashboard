from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.urls import include
from rest_framework import routers

from blog import views as blog_views

router = routers.DefaultRouter()

# Blog endpoints
router.register(
    r'posts',
    blog_views.PostViewSet,
    basename='posts'
)


urlpatterns = [
    # Admin site
    path("admin/", admin.site.urls),
    
    # Redirects
    path(
        '',
        RedirectView.as_view(url='/admin/'),
        name='home-redirect-admin'
    ),
    path(
        'accounts/login/',
        RedirectView.as_view(url='/admin/'),
        name='login-redirect-admin'
    ),
    
    # API URLs
    path('api/', include(router.urls)),
]


if not settings.STORAGE_AWS:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
