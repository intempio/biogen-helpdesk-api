from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path, reverse_lazy
from django.views.generic.base import RedirectView
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .events.views import AttendeeViewSet, EventAttendeeViewSet, EventViewSet, UpTimeView, EventLookRedirectView
from .users.views import UserCreateViewSet, UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'users', UserCreateViewSet)
router.register(r'events', EventViewSet)
router.register(r'attendees', AttendeeViewSet)
router.register(r'event-attendees', EventAttendeeViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('redirect/<event_id>/', EventLookRedirectView.as_view()),
    path('uptime/', UpTimeView.as_view()),

    # the 'api-root' from django rest-frameworks default router
    # http://www.django-rest-framework.org/api-guide/routers/#defaultrouter
    re_path(r'^$', RedirectView.as_view(url=reverse_lazy('api-root'), permanent=False)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
