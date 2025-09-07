from .models import *
from rest_framework import serializers

class LoginSerializer(serializers.Serializer):
    username=serializers.CharField(max_length=10)
    password=serializers.CharField(max_length=10)



class SignupSerializer(serializers.ModelSerializer):
    
    password=serializers.CharField(write_only=True)
    confirm_password=serializers.CharField(write_only=True)

    class Meta:
        model=User
        fields=['username','email','password','confirm_password']

    def validate(self,data):
        if data['password'] !=data['confirm_password']:
            raise serializers.ValidationError("password not match")
        return data
        
    def create(self,validate_data):
        validate_data.pop('confirm_password')
        user=User.objects.create_user(**validate_data)
        return user
    


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model=Teacher
        fields='__all__'


 ###nested reverse relationship getting classrooms  with all  their students details

class StudentMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["id", "name"]

class ClassroomNestedSerializer(serializers.ModelSerializer):
    students=StudentMiniSerializer(many=True,read_only=True)

    class Meta:
        model=Classroom
        fields=['id','name','students']


####get student detail with classroom name
class StudentwithClassRoom(serializers.ModelSerializer):
    classroom=serializers.CharField(source="classroom.name",read_only=True)

    class Meta:
        model=Student
        fields=["id","name","classroom"]


###get all subjects with their teacher and students
class GetSubject(serializers.ModelSerializer):
    student=StudentSerializer(many=True,read_only=True)
    teacher=TeacherSerializer( read_only=True)

    class Meta:
        model=Subject
        fields=['id','name','teacher','student','classroom']