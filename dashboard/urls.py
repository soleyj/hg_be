from django.urls import path,include
from rest_framework import routers
from dashboard import views
from .api import MachineDataViewSet,ExampleView

router = routers.DefaultRouter()
router.register('data_hg',MachineDataViewSet,'sensor')


urlpatterns = [ 
    path('api/', include(router.urls)),
    path('api/example/', ExampleView.as_view(), name="ExampleView"),
]





app_name = 'dashboard'