from django.urls import path
from .views import *

urlpatterns = [
    path('login/',login_view,name='login'),
    path('signup/',signup_view,name='signup'),

    path('student/',student_get_post,name='student'),
    path('students/<int:id>/',student_details,name='student_details'),

    path('subject_add_student/<int:id>/',register_subject,name='register_subject'),

    path('classroom/',classroom_detail,name='classroom_detail'),

    path('students_with_cr/',student_with_classroom,name='studentwithcr'),

    path('subjects/',subject_detail,name='subject_detail'),
]