from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Student, Teacher
from .serializers import StudentSerializer, TeacherSerializer

@api_view(['POST', 'GET'])
def register_student(request):
    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)


@api_view(['POST', 'GET'])
def register_teacher(request):
    if request.method == 'POST':
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def login_user(request):
    print("Login data:", request.data)

    role = request.data.get('role')
    email = request.data.get('email')
    password = request.data.get('password')

    try:
        if role == 'student':
            user = Student.objects.get(email=email)
        elif role == 'teacher':
            user = Teacher.objects.get(email=email)
        else:
            return Response({'error': 'Invalid role'}, status=400)

        from django.contrib.auth.hashers import check_password
        if check_password(password, user.password):
            return Response({'message': 'Login successful', 'role': role, 'user_id': user.id})
        else:
            return Response({'error': 'Invalid credentials'}, status=401)

    except (Student.DoesNotExist, Teacher.DoesNotExist):
        return Response({'error': 'User not found'}, status=404)

    except Exception as e:
        print("Server error:", str(e))
        return Response({'error': 'Server error'}, status=500)
