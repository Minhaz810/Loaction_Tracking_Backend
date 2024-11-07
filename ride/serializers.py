from rest_framework import serializers
from .models import Tips,AdminEarning

class TipsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tips
        fields = '__all__' 

class AdminEarningSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminEarning
        fields = '__all__' 