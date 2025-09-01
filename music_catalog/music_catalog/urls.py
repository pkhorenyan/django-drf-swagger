from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from catalog.views import ArtistViewSet, AlbumViewSet, SongViewSet, AlbumSongViewSet, index

router = DefaultRouter()
router.register(r'artists', ArtistViewSet)
router.register(r'albums', AlbumViewSet)
router.register(r'songs', SongViewSet)
router.register(r'album-songs', AlbumSongViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Music Catalog API",
        default_version="v1",
        description="API для каталога исполнителей, альбомов и песен",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('', index, name="home"),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name="swagger-ui"),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name="redoc-ui"),
    path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
]

