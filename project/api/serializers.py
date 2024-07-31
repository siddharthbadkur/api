from  rest_framework import serializers
from .models import *



# class studentSerializer(serializers.Serializer):
#     stu_name=serializers.CharField(max_length=45)
#     stu_email=serializers.EmailField(max_length=33)
#     stu_contact=serializers.IntegerField()
#     stu_city=serializers.CharField(max_length=50)

#     def create(self, validated_data):
#         """
#         Create and return a new `Snippet` instance, given the validated data.
#         """
#         return Studentapi.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Snippet` instance, given the validated data.
#         """
#         instance.stu_name = validated_data.get('title', instance.stu_name)
#         instance.stu_email = validated_data.get('code', instance.stu_email)
#         instance.stu_contact = validated_data.get('linenos', instance.stu_contact)
#         instance.stu_city = validated_data.get('language', instance.stu_city)
class Studentserializer(serializers.ModelSerializer):
    class Meta:
        model=Studentapi
        fields=["id","stu_name","stu_city","stu_contact","stu_email"]
