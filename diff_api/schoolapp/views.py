from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from django.contrib.auth import authenticate,login,logout
from rest_framework import status
# Create your views here.

@api_view(['POST'])
def login_view(request):
    serializers=LoginSerializer(data=request.data)
    
    if serializers.is_valid():
        username=serializers.validated_data['username']
        password=serializers.validated_data['password']
        user=authenticate(username=username,password=password)
        login(request,user)
        return Response({"msg":"login sucess"},status=200)
    return Response(serializers.errors)



@api_view(["POST"])
def signup_view(request):
    serializers=SignupSerializer(data=request.data)
    if serializers.is_valid():
        
        user=serializers.save()
        return Response(
            {"message": "User created successfully", "username": user.username, "email": user.email},
            status=status.HTTP_201_CREATED
        )
    return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)



#for admin to get ,create,edit,delete student details
@api_view(["GET","POST"])
def student_get_post(request):
    if request.method=="GET":
        student=Student.objects.all()
        serializers=StudentSerializer(student,many=True)
        return Response(serializers.data,status=status.HTTP_200_OK)
    
    elif request.method=="POST":
        serializers=StudentSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['GET','PUT','DELETE'])
def student_details(request,id):
    if request.method=='GET':
        student=Student.objects.get(id=id)
        serializers=StudentSerializer(student)
        return Response(serializers.data)
    
    elif request.method=='PUT':
        student=Student.objects.get(id=id)
        serializers=StudentSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_202_ACCEPTED)
        return Response(serializers.errors)
    

    elif request.method=="DELETE":
        student=Student.objects.get(id=id)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

#students for registering for subject


@api_view(['POST','GET'])
def register_subject(request,id):
    try:
       subject=Subject.objects.get(id=id)
    except Subject.DoesNotExist():
        return Response({"error":"subject not exist"},status=status.HTTP_404_NOT_FOUND)
    
    user=request.user
    student=Student.objects.get(user=user)
    
    if subject.student.filter(id=student.id).exists():
        return Response({"msg": f"{student.user.username} is already registered for {subject.name}"},
                        status=status.HTTP_200_OK)
     
    subject.student.add(student)
    return Response({"msg":f"{student.user.username} registered for {subject.name}"})


#getting all classroom with their students

@api_view(["GET"])
def classroom_detail(request):
    classrooms = Classroom.objects.all()
    serializer = ClassroomNestedSerializer(classrooms, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


#getting student with their classroom

@api_view(['GET'])
def student_with_classroom(request):
    students=Student.objects.all()
    serializers=StudentwithClassRoom(students,many=True)
    return Response(serializers.data)



#getting all subjects with their student and teacher details
@api_view(['GET'])
def subject_detail(request):
    subject=Subject.objects.all()
    serializers=GetSubject(subject,many=True)
    return Response(serializers.data)