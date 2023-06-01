from django.contrib import admin
from .models import Tutorial,PayedCourse, Course, CourseContent,Vlog,Comment,PCourseContent,PurchasedCourse,UserSection,pays

admin.site.register(Course)
admin.site.register(CourseContent)
admin.site.register(PayedCourse)

admin.site.register(Tutorial)
admin.site.register(pays)

admin.site.register(Vlog)
admin.site.register(Comment)
admin.site.register(PCourseContent)
admin.site.register(PurchasedCourse)
admin.site.register(UserSection)
