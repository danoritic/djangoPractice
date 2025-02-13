from rest_framework import serializers 
from .models import Member, Property
class PropertySerializer(serializers.ModelSerializer): 
     class Meta:
        model = Property
        fields = '__all__'
class MemberSerializer(serializers.ModelSerializer):
    # votes = VoteSerializer(many=True, required=False)
    class Meta:
        model = Member
        fields = '__all__'
