from django.shortcuts import get_object_or_404, render
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
        serializers=StudentSerializer(student,data=request.data)
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



###student updating their student record
@api_view(['PATCH'])
def student_selfupdate(request,id):
    
    student=Student.objects.get(id=id)
     
    serializers=StudentUpdate(student,data=request.data,partial=True)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data)
    return Response(serializers.errors)


###teacher updating detail
@api_view(['PATCH','PUT'])
def teacher_update(request,id):
    try:
        teacher=Teacher.objects.get(id=id)
    except Teacher.DoesNotExist:
        return Response({"error":"Teacher does not exist"},status=status.HTTP_404_NOT_FOUND)
    
    user=request.user
    data=request.data.copy()
    data['user']=user.id
    serializers=TeacherSerializer(teacher,data=data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data)
    return Response(serializers.errors)


###student able to see his teacher details
@api_view(['GET'])
def student_teacher(request):
    student=Student.objects.get(user=request.user)
    teacher=Teacher.objects.filter(subject__student=student)
    serializers=TeacherSerializer(teacher,many=True)
    return Response(serializers.data)


###teacher will able to see the students registered under him 
@api_view(['GET'])
def teacher_student(request):
    teacher=get_object_or_404(Teacher,user=request.user)
    student=Student.objects.filter(subject__teacher=teacher)
    serializers=StudentSerializer(student,many=True)
    return Response(serializers.data)


###crud operation on Teacher by admin
@api_view(["GET","POST"])
def Teacher_Details(request):
    if request.method=="GET":
        teacher=Teacher.objects.all()
        serializers=TeacherSerializer(teacher,many=True)
        return Response(serializers.data,status=status.HTTP_200_OK)
    
    elif request.method=="POST":
        serializers=TeacherSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET','PUT','DELETE'])
def teachers(request,id):
    try:
        teacher=Teacher.objects.get(id=id)
    except Teacher.DoesNotExist:
        return Response({"error":"teacher not found"})
    

    if request.method=="GET":
        serializers=TeacherSerializer(teacher)
        return Response(serializers.data,status=status.HTTP_200_OK)
    
    elif request.method=="PUT":
        serializers=TeacherSerializer(teacher,data=request.data,partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    

    elif request.method=="DELETE":
        teacher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(["POST"])
def search_subject(request):
    search=request.data.get('search','')
    subject=Subject.objects.filter(name__icontains=search)
    serializers=GetSubject(subject,many=True)
    return Response(serializers.data)





@api_view(['POST'])
def create_timetable(request):
    serializers=TimeTableWriteSerializer(data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data)
    return Response(serializers.errors)


@api_view(['GET'])
def get_timetable(request):
    tt=TimeTable.objects.all()
    serializers=TimeTableReadSerializers(tt,many=True)
    return Response(serializers.data,status=status.HTTP_200_OK)


@api_view(['POST'])
def teacher_create_tt(request):
    teacher=Teacher.objects.get(user=request.user)
    data=request.data.copy()
    data['teacher']=teacher.id
    subject_id=request.data.get('subject_id')
    classroom_id=request.data.get('classroom_id')
    days=request.data.get('days')
    time=request.data.get('time')


    subject = get_object_or_404(Subject, id=subject_id)
    classroom = get_object_or_404(Classroom, id=classroom_id)

    timetable=TimeTable.objects.create(
        teacher=teacher,
        classroom=classroom,
        subject=subject,
        days=days,
        time=time
    )
    return Response(
            {
                "id": timetable.id,
                "subject": subject.name,
                "classroom": classroom.name,
                "teacher": teacher.name,
                "days": days,
                "time": time,
            },
            status=status.HTTP_201_CREATED,
        )

### get timetable by subjectwise
@api_view(["GET"])
def tt_by_sub(request,id):
    subject=Subject.objects.get(id=id)
    tt=TimeTable.objects.filter(subject=subject)
    serializers=TimeTableReadSerializers(tt,many=True)
    return Response(serializers.data,status=status.HTTP_200_OK)

###get timetable by time-at a given time
@api_view(['POST'])
def tt_by_time(request):
    search=request.data.get('time','')
    tt=TimeTable.objects.filter(time__icontains=search)
    serializers=TimeTableReadSerializers(tt,many=True)
    return Response(serializers.data)



###get timetable by time-at a given day
@api_view(['POST'])
def tt_by_timeandday(request):
    search=request.data.get('time','')
    search1=request.data.get('days','')
    tt=TimeTable.objects.filter(time__icontains=search,days__icontains=search1)
    serializers=TimeTableReadSerializers(tt,many=True)
    return Response(serializers.data)



