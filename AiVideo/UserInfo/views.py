from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from django import http
from .models import *
import datetime

def index(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return http.HttpResponse(html)


def add_user(request):

    username = request.POST.get('username')
    password = request.POST.get('password')
    user_kind = request.POST.get("user_kind")
    print('username',username)
    if username == "" or password == "":
        # 不能添加数据
        return http.HttpResponse(json.dumps({"code": 400, "msg": "用户名或密码不能为空"}))
    else:
        #  用户名不为空
        num = UserInfo.objects.filter(username=username).count()
        if num <= 0:
            # 数据库用户名不存在，添加数据
            UserInfo.objects.create(username=username, password=password,user_kind=user_kind)
            return http.HttpResponse(json.dumps({"code": 200, "msg": "添加数据成功"}))
        else:
            return http.HttpResponse(json.dumps({"code": 500, "msg": "用户名已存在，请直接登陆"}))

def check_userinfo(request):

    username = request.GET.get("username")
    password = request.GET.get("password")

    try:
        new_name = UserInfo.objects.get(username=username)
    except Exception as e:
        print(e)
        return http.HttpResponse(json.dumps({"code": 400, "msg": "用户名或密码不存在"}))
        # 在try正长执行，才会执行else
    else:
        # 判断login中，用户名是否存在
        if new_name == "":
            return http.HttpResponse(json.dumps({"code": 500, "msg": "用户名或密码错误"}))
        else:

            if new_name.password == password:
                print('123456',new_name.to_dict())
                return http.HttpResponse(json.dumps({"code": 200, "msg": new_name.to_dict()}))
    # else:
    #     return HttpResponse(json.dumps({"code":400,"msg":"用户名或密码不存在"}))


def update_password(resquest):
    username = resquest.POST.get('username')
    password = resquest.POST.get('password')
    repassword = resquest.POST.get('repassword')

    user_data = UserInfo.objects.filter(username=username)
    if user_data == "":
        return http.HttpResponse(json.dumps({"code": 500, "msg": "用户名不存在"}))
    else:
        if password == repassword:
            user_data.update(password=password)

            return http.HttpResponse(json.dumps({"code": 200, "msg": "用户名和密码正确，登录首页"}))
        else:
            return http.HttpResponse(json.dumps({"code": 500, "msg": "两次密码不一样"}))
@csrf_exempt
def is_first_login(request):
    new_user_id = request.GET.get("user_id")
    print("new_user_id",new_user_id)
    user_kind = UserInfo.objects.get(user_id=new_user_id).user_kind
    if user_kind == "学生":
        try:
            Student.objects.get(s_u_id=new_user_id)
            return http.HttpResponse(json.dumps({"code": 500, "msg": "信息已存在，登录首页"}))
        except Exception as e:
            return http.HttpResponse(json.dumps({"code": 200, "msg": "可以填写信息，登录首页"}))
    else:
        try:
            Teacher.objects.get(t_u_id=new_user_id)
            return http.HttpResponse(json.dumps({"code": 500, "msg": "信息已存在，登录首页"}))
        except Exception as e:
            return http.HttpResponse(json.dumps({"code": 200, "msg": "可以填写信息，登录首页"}))
@csrf_exempt
def regist_student_info(request):
    user_stu_id = request.POST.get("user_id")
    student_num = request.POST.get("student_num")
    student_name = request.POST.get("student_name")
    student_age = request.POST.get("student_age")

    try:
        Student.objects.get(s_u_id=user_stu_id)
        return http.HttpResponse(json.dumps({"code": 500, "msg": "已经存在数据"}))
    except Exception as e:
        print(user_stu_id,student_num,student_name,student_age)
        Student.objects.create(student_num=student_num, student_name=student_name,student_age=student_age,s_u_id=user_stu_id)
        return http.HttpResponse(json.dumps({"code": 200, "msg": "用户名和密码正确，登录首页"}))


@csrf_exempt
def regist_teacher_info(request):
    user_tea_id = request.POST.get("user_id")
    teacher_num = request.POST.get("teacher_num")
    teacher_name = request.POST.get("teacher_name")
    teacher_age = request.POST.get("teacher_age")
    try:
        teacher_data = Teacher.objects.get(t_u_id=user_tea_id)
        return http.HttpResponse(json.dumps({"code": 500, "teacher_num": teacher_data.teacher_num}))
    except Exception as e:
        print(e)
        print(user_tea_id,teacher_num,teacher_name,teacher_age)
        Teacher.objects.create(teacher_num=teacher_num, teacher_name=teacher_name,teacher_age=teacher_age,t_u_id=user_tea_id)
        return http.HttpResponse(json.dumps({"code": 200, "msg": "用户名和密码正确，登录首页"}))




@csrf_exempt
def regist_course_info(request):
    course_name = request.POST.get("course_name")

    if course_name == "" :
        # 不能添加数据
        return http.HttpResponse(json.dumps({"code": 400, "msg": "课程名不能为空"}))
    else:
        #  用户名不为空
        num = Course.objects.filter(course_name=course_name).count()
        if num <= 0:
            # 数据库用户名不存在，添加数据
            Course.objects.create(course_name=course_name)
            return http.HttpResponse(json.dumps({"code": 200, "msg": "添加数据成功"}))
        else:
            return http.HttpResponse(json.dumps({"code": 500, "msg": "用户名已存在，请直接登陆"}))
def get_course(request):
    course_datas = Course.objects.all()
    datas = []
    for index,i in enumerate(course_datas):
        data = {}
        data["course_id"] = i.course_id
        data["course_name"] = i.course_name
        datas.append(data)
    print(datas)
    print(json.dumps(datas))
    return http.HttpResponse(json.dumps(datas))
@csrf_exempt
def update_tea_course(request):
    user_t_id = request.POST.get("user_id")
    c_id = request.POST.get("c_id_data")
    print(user_t_id,c_id)
    tea_data = Teacher.objects.filter(t_u_id=user_t_id)
    tea_data.update(ts_cour_id=c_id)

    return http.HttpResponse(json.dumps({"code": 200, "msg": "选课成功，登录首页"}))

def get_all_tea_cour(request):

    all_tea_cour_data = Teacher.objects.all()
    datas = []
    for i in all_tea_cour_data:
        data = {}
        data["teacher_id"] = i.teacher_id
        data["teacher_name"] = i.teacher_name
        data["ts_cour_id"] = i.ts_cour_id
        data["course_name"] = Course.objects.get(course_id=i.ts_cour_id).course_name
        datas.append(data)

    print(datas)
    return http.HttpResponse(json.dumps( datas))

def render_page(request, page_name):
    return render(request, '{}'.format(page_name))










