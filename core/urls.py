
from django.urls import path,include
from core import views

urlpatterns = [
    path('student', views.StudentAPIView.as_view()),
    path('students', views.StudentAPIRequest.as_view()),
    
    
]