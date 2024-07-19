from rest_framework import routers
from .views import *
from django.conf.urls.static import static

app_name = "formapp"

router = routers.DefaultRouter()
router.register(r'formapp', FormDataView)
urlpatterns = router.urls
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

