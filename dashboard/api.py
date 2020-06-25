from dashboard.models import machine_hw, data_hg
from rest_framework import viewsets, permissions,generics
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import MachineDataSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

##Sensor viewset
class MachineDataViewSet(viewsets.ModelViewSet):
    queryset = data_hg.objects.all()
    permission_classes =[
        permissions.AllowAny
    ]
    
    serializer_class = MachineDataSerializer
    filter_fields = ('machine__id_machine',)  

    @action(methods = ['get'],detail= False)
    def newest(self,request):
        newest = self.get_queryset().order_by('id').last()
        serializer = self.get_serializer_class()(newest)
        return Response(serializer.data)


class ExampleView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        return Response(content)