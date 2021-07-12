from rest_framework import serializers
from .models import Contact

# serializers class for model class 
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
