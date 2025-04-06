from rest_framework.serializers import Serializer,ModelSerializer
from rest_framework import serializers
from .models import School,Teacher,Student

class SchoolSerailzer(serializers.ModelSerializer):
    class Meta:
        model=School
        fields='__all__'
    def validate(self,data):
        name=data.get('name')
        address=data.get('address')
        if School.objects.filter(name=name,address=address).exists():
            raise  serializers.ValidationError("A school with same name and address already exists.")
        return data
        
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model=Teacher
        fields='__all__'

    # def validate(self, data):
    #     name=data['name']
    #     subject=data['subject']
    #     school=data['school']
    #     if Teacher.objects.filter(name=name,subject=subject,school=school).exists():
    #         raise serializers.ValidationError("Same teacher can not teach different subjects at different school.")
    #     return data

class StudentSerailzer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'

    def validate(self, data):
        age = data.get('age')
        if age is not None:  
            if age < 3 or age > 30:  
                raise serializers.ValidationError('Age must be between 3 and 60.')
        return data