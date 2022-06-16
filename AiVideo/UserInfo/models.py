from django.db import models

# Create your models here.
class UserInfo(models.Model):
    user_id = models.IntegerField(max_length=32,primary_key=True)
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    user_kind = models.CharField(max_length=16)

    def to_dict(self):
        return {
            'id': self.user_id,
            'username': self.username,
            'user_kind':self.user_kind,
        }

    # class Meta:
    #

class Student(models.Model):
    student_id = models.IntegerField(max_length=32,primary_key=True)
    student_num = models.CharField(max_length=16)
    student_name = models.CharField(max_length=16)
    student_age = models.CharField(max_length=16)
    s_u = models.ForeignKey(UserInfo,on_delete=models.CASCADE,related_name="u_s")


class Course(models.Model):
    course_id = models.IntegerField(max_length=32,primary_key=True)
    course_name = models.CharField(max_length=16)
class Teacher(models.Model):
    teacher_id = models.IntegerField(max_length=32, primary_key=True)
    teacher_num = models.CharField(max_length=16)
    teacher_name = models.CharField(max_length=16)
    teacher_age = models.CharField(max_length=16)
    t_u = models.ForeignKey(UserInfo,on_delete=models.CASCADE,related_name="u_t")
    ts_cour = models.ForeignKey(Course,blank=True,null=True,on_delete=models.CASCADE,related_name="c_teas")

class StuCourse(models.Model):
    s_stus = models.ManyToManyField(Student, related_name='c_cours')
    c_id = models.IntegerField(primary_key=True)
    t_id = models.IntegerField()