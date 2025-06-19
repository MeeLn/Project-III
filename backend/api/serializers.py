from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Student, Teacher

class StudentSerializer(serializers.ModelSerializer):
    rollNo = serializers.CharField(source='roll_no')
    firstName = serializers.CharField(source='first_name')
    lastName = serializers.CharField(source='last_name')
    confirmPassword = serializers.CharField(write_only=True)  # we don't need to save this

    class Meta:
        model = Student
        fields = [
            'rollNo', 'firstName', 'lastName', 'email',
            'phone', 'address', 'faculty', 'password', 'confirmPassword'
        ]

    def validate(self, data):
        if data['password'] != data['confirmPassword']:
            raise serializers.ValidationError("Passwords do not match")
        return data

    def create(self, validated_data):
        validated_data.pop('confirmPassword')  # Remove confirmPassword before saving
        validated_data['password'] = make_password(validated_data['password'])  # Hash password
        return Student.objects.create(**validated_data)


class TeacherSerializer(serializers.ModelSerializer):
    firstName = serializers.CharField(source='first_name')
    lastName = serializers.CharField(source='last_name')
    confirmPassword = serializers.CharField(write_only=True)

    class Meta:
        model = Teacher
        fields = [
            'firstName', 'lastName', 'email',
            'phone', 'address', 'password', 'confirmPassword'
        ]

    def validate(self, data):
        if data['password'] != data['confirmPassword']:
            raise serializers.ValidationError("Passwords do not match")
        return data

    def create(self, validated_data):
        validated_data.pop('confirmPassword')  # Remove confirmPassword before saving
        validated_data['password'] = make_password(validated_data['password'])  # Hash password
        return Teacher.objects.create(**validated_data)
