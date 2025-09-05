from django.urls import path
from .views import *

urlpatterns = [
    path('login/',login_view,name='login'),
    path('signup/',signup_view,name='signup'),

    path('student/',student_get_post,name='student'),
    path('students/<int:id>/',student_details,name='student_details'),
]