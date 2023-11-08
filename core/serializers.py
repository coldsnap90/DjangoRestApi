from core.models import Student
from rest_framework import serializers




class StudentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Student
        fields = ['id','password','last_login','is_superuser','username','first_name','last_name','email','is_staff','is_active','date_joined']