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

    path('student_update/<int:id>/',student_selfupdate,name='student_update'),

    path('teacher_update/<int:id>/',teacher_update,name='teacher_update'),

    path('stud/',student_teacher,name='student_teacher'),

    path('teach/',teacher_student,name='teach'),

    path('teacher/',Teacher_Details,name='teacher'),

    path('teachers/<int:id>/',teachers,name='teachers')
]