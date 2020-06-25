from rest_framework import serializers
from dashboard.models import machine_hw, data_hg

#Lead Serializer
class MachineDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = data_hg
        fields = "__all__"

class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = machine_hw
        fields = "__all__"