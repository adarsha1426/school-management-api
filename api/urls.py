from django.urls import path
from .serializers import SchoolSerailzer,TeacherSerializer,StudentSerailzer
from . import views
urlpatterns = [
    # path('login/',views.login,name='login'),
    path('schools/',views.school,name='school'),
    path('schools/<int:id>/',views.school_update,name='update_school'),
    path('teachers/',views.teacher,name='teaches'),
    path('teachers/<int:id>/',views.teacher_update,name='update_teacher'),
    path('students/',views.students,name='student'),
    path('students/<int:id>/',views.students_update,name='update_student'),
    path('search',views.search,name='search'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('paginationdemo/',views.school_list,name='pagination')
]
