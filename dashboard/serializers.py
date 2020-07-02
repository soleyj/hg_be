from rest_framework import serializers
from dashboard.models import machine_hw, data_hg, data_hg_outputs, data_hg_confgi

#Lead Serializer
class MachineDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = data_hg
        fields = "__all__"

class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = machine_hw
        fields = "__all__"
    
class OutputsSerializer(serializers.ModelSerializer):
    class Meta:
        model = data_hg_outputs
        fields = "__all__"



class ConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = data_hg_confgi
        fields = "__all__"