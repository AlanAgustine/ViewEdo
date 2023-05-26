from django.db import models
from docx import Document
from io import BytesIO

class Tutorial(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='thumbnails/', null=True, blank=True)
    video = models.FileField(upload_to='videos/', null=True, blank=True)

    def __str__(self):
        return self.title

    @classmethod
    def latest_id(cls):
        latest_tutorial = cls.objects.latest('id')
        return latest_tutorial.id



from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    software_icon = models.ImageField(upload_to='software_icons/')
    created_at = models.DateTimeField(auto_now_add=True, null= True)

    def __str__(self):
        return self.title



class CourseContent(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title
    

    
 
    

    





from django.db import models
from django.utils import timezone

class PayedCourse(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='course_images/')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(default=timezone.now, null=True)

    def __str__(self):
        return self.title
    

class PCourseContent(models.Model):
    course = models.ForeignKey(PayedCourse, on_delete=models.CASCADE, related_name='course_content')
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title



from django.contrib.auth.models import User
from django.db import models

class PurchasedCourse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(PayedCourse, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)

from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    purchased_courses = models.ManyToManyField(PayedCourse)

    # Add any additional fields or methods you need for the user profile

    def __str__(self):
        return self.user.username

    

from django.db import models
from django.contrib.auth.models import User

class UserSection(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
    

from django.contrib.auth.models import User
from django.db import models
from .models import Course

class FavoriteCourse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

# models.py
from django.contrib.auth.models import User
from django.db import models


class MyCourse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'course')

    def __str__(self):
        return f"{self.user.username} - {self.course.title}"    
    




from django.contrib.auth.models import User


class Vlog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    image = models.ImageField(upload_to='vlogs/')
    title = models.CharField(max_length=200)
    details = models.TextField()
    date = models.DateField()
   

    def __str__(self):
        return self.title
    

from django.db import models

from django.db import models

class Comment(models.Model):
    name = models.CharField(max_length=100)  # Add the name field
    email = models.EmailField()
    website = models.URLField(blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



