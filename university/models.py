from django.db import models

# Create your models here.

class Students(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length= 50 )
    email = models.EmailField()
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Course(models.Model):
    name = models.CharField(max_length = 50)
    description = models.TextField()
    students= models.ManyToManyField(
        Students,
        related_name='courses'
    )




student1 = Students.objects.create(first_name = 'Alihan', last_name = 'Mahachbekov' , email = 'alian@gmail.com', age = 80)
student2 = Students.objects.create(first_name = 'Monster', last_name = 'Malikov' , email = 'maria12@gmail.com' , age= 10)
course1 = Course.objects.create(name= 'programing', description= 'fsdfsadfjasfsd' ,)
course2 = Course.objects.create(name= 'math', description= 'fsdfsadfjasfsd')
student1.courses.set([course1 , course2])
student1.courses.all()
# <QuerySet [<Course: Course object (1)>, <Course: Course object (2)>]>
course1.students.set([student1, student2])
course1.students.all()
# <QuerySet [<Students: Students object (2)>, <Students: Students object (3)>]>