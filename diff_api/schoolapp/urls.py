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

    path('teachers/<int:id>/',teachers,name='teachers'),

    path('search/',search_subject,name='search'),
    path('create_tt/',create_timetable,name='create_tt'),

    path('tt/',get_timetable,name='tt'),

    path('tttt/',teacher_create_tt,name='tttt'),

    path('ttbs/<int:id>/',tt_by_sub,name='ttbs'),

    path('ttbt/',tt_by_time,name='ttbt'),


    path('ttbtd/',tt_by_timeandday,name='tttbtd'),
    path('tt_get/',tt_get,name='tt_get'),

    path('exam/',create_getexam,name='exam'),


    path('exams/<int:id>/',get_update_delexam,name='exams'),
    path('stud_exam/',student_exam,name='stude'),

    path('exam_s/',exam_search,name='exams'),

    path('examss/',exam_search2,name='examss'),
    path('countt/',sub_countTT,name='countt'),
]