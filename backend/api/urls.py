from django.urls import path
from . import views

urlpatterns = [
    path('register/student/', views.register_student),
    path('register/teacher/', views.register_teacher),
    path('login/', views.login_user),
]
