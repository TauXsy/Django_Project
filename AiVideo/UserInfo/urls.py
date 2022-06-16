"""AiVideo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import *
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('add_user/',add_user,name='add_user'),
    path('check_userinfo/',check_userinfo,name='check_userinfo'),
    path('update_password/',update_password,name='update_password'),
    path('regist_student_info/',regist_student_info,name='regist_student_info'),
    path('regist_teacher_info/',regist_teacher_info,name='regist_teacher_info'),
    path('regist_course_info/',regist_course_info,name='regist_course_info'),
    path('is_first_login/',is_first_login,name='is_first_login'),
    path('get_course/',get_course,name='get_course'),
    path('update_tea_course/',update_tea_course,name='update_tea_course'),
    path('get_all_tea_cour/',get_all_tea_cour,name='get_all_tea_cour'),
    path('page/<str:page_name>/', render_page, name='page'),
]
