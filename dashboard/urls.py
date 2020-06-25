from django.urls import path
from rest_framework import routers
from dashboard import views
from .api import MachineDataViewSet

router = routers.DefaultRouter()
router.register('api/data_hg',MachineDataViewSet,'sensor')

urlpatterns = router.urls

app_name = 'dashboard'