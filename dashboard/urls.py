from django.urls import path,include
from rest_framework import routers
from dashboard import views
from .api import MachineDataViewSet,ExampleView,HgDataOutput, HgDataConfig

router = routers.DefaultRouter()
router.register('data_hg',MachineDataViewSet,'sensor')
router.register('data_output',HgDataOutput,'output')
router.register('data_input',HgDataConfig,'HgDataConfig')

urlpatterns = [ 
    path('api/', include(router.urls)),
    path('api/example/', ExampleView.as_view(), name="ExampleView"),
    
]





app_name = 'dashboard'