
from django.urls import path,include
from core import views

urlpatterns = [
    path('student', views.StudentAPIView.as_view(),name='students'),
    path('student<int:pk>', views.StudentDetailView.as_view(),name='students_id'),
    
    
]