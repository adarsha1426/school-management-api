from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from .models import School,Teacher,Student
from django.shortcuts import get_object_or_404
from .serializers import SchoolSerailzer,StudentSerailzer,TeacherSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.pagination import PageNumberPagination
# Create your views here.
def home(request):
    return Response({'hello':'hello'},status=status.HTTP_200_OK)

@api_view(['GET','POST'])
def school(request):
    if request.method=='POST':
        serializer=SchoolSerailzer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
    elif request.method=='GET':
        school=School.objects.all()
        serializer=SchoolSerailzer(school,many=True)
        return Response({"schools":serializer.data})
    else:
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT','DELETE'])
def school_update(request,id):
    school=get_object_or_404(School,id=id)
    if request.method=='PUT':
        if school is None:
            return Response({"message":"School not found"})
        else:
            serializer=SchoolSerailzer(school,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'school':serializer.data})
    else:
        school.delete()
        return Response({'message':f'{school.name} has been deleted'})
#for teachers
@api_view(['GET','POST'])
def teacher(request):
    if request.method=='POST':
        serializer=TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
    elif request.method=='GET':
        teacher=Teacher.objects.all()
        serializer=TeacherSerializer(teacher,many=True)
        return Response({"schools":serializer.data})
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT','DELETE'])
def teacher_update(request,id):
    teacher=get_object_or_404(Teacher,id=id)
    if request.method=='PUT':
        if teacher is None:
            return Response({"message":"School not found"})
        else:
            serializer=TeacherSerializer(teacher,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'teacher':serializer.data})
    else:
        teacher.delete()
        return Response({'message':f'{teacher.name} has been deleted'})
#for students
@api_view(['GET','POST'])
def students(request):
    if request.method=="POST":
        serializer=StudentSerailzer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'students':serializer.data},status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
    elif request.method=="GET":
        students=Student.objects.all()
        serializer=StudentSerailzer(students,many=True)
        return Response({'students':serializer.data},status=status.HTTP_200_OK)
    return Response(serializer.errors)

@api_view(['PUT','DELETE'])
def students_update(request,id):
    students=get_object_or_404(Student,id=id)
    if request.method=="PUT":
        serializer=StudentSerailzer(students,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'students':serializer.data},status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
    elif request.method=="DELETE":
        students.delete()
        return Response(f'{students.name} has been deleted',status=status.HTTP_200_OK )
    
#searching students
@api_view(['GET'])
def search(request):
    query = request.GET.get('q')
    if not query:
        return Response({'error': 'Invalid query'}, status=status.HTTP_400_BAD_REQUEST)
    students = Student.objects.filter(name__iexact=query)
    output=[]
    for student in students:
        output.append({
            'student_name':student.name,
            'student_age':student.age,
            'student_grade':student.grade,
            'school_name':student.school.name,
            'school_address':student.school.address,
        })
    return Response({
        'data':output,
    }, status=status.HTTP_200_OK)

@api_view(['POST'])
def login(request):
    username=request.data.get('username')
    password=request.data.get('password')
    user=authenticate(username=username,password=password)
    if user:
        refresh=RefreshToken.for_user(user)
        return Response({'refresh':str(refresh),
                         'access':str(refresh.access_token)})
    else:
        return Response({'message':'Invalid Username and Password'},status=status.HTTP_400_BAD_REQUEST)
@api_view(['POST'])
def register(request):
    username=request.data.get('username')
    password=request.data.get('password')
    if User.objects.filter(username=username).exists():
        return Response({'message':'User with username already exists'},status=status.HTTP_400_BAD_REQUEST)
    user=User.objects.create_user(username=username,password=password)
    return Response({'message':'User registered successfully.'},status=status.HTTP_201_CREATED)
    
@api_view(['GET'])
def school_list(request):
    schools=School.objects.all()
    paginator= PageNumberPagination()
    paginator.page_size= 3 #we have small database so
    result_page = paginator.paginate_queryset(schools, request)
    serializer = SchoolSerailzer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)