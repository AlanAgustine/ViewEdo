from django.urls import path
from . import views
from .views import software_list
from .views import course_detail
from.views import logout_view
from.views import delete_vlog
from.views import add_comment
from.views import blog
from.views import purchased_courses
from.views import buy_course





app_name = 'photoedit'

urlpatterns = [
    path('', views.index, name='index'),
    path('tutorial/<int:tutorial_id>/', views.tutorial, name='tutorial'),
    path('about/', views.about, name='about'),
    path('base/', views.base, name='base'),
    path('sidebar/', views.sidebar, name='sidebar'),
    path('detail/<int:tutorial_id>/', views.detail, name='detail'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('sflist/', software_list, name='software_list'),
    path('course/<int:pk>/', course_detail, name='course_detail'),
    path('p_course/', views.p_course, name='p_course'),
    path('logout/', logout_view, name='logout'),
    path('p_details/<int:pk>',views.p_detail, name='p_details'),
    path('p_details/<int:course_id>', views.purchase_course, name='purchase_course'),
    path('add_course/<int:course_id>/', views.add_course, name='add_course'),
    path('courses/', views.courses, name='courses'),
    path('my_courses/', views.my_courses, name='my_courses'),
    path('remove_course/<int:my_course_id>/', views.remove_course, name='remove_course'),
    path('purchase_course/<int:course_id>/', views.purchase_course, name='purchase_course'),
    path('search/', views.search_view, name='search'),
    path('blog/', views.blog, name='blog'),
    path('add_vlog/', views.add_vlog, name='add_vlog'),
    path('vlog/delete/<int:vlog_id>/', delete_vlog, name='delete_vlog'),
    path('course/<int:pk>/add_comment/', views.add_comment, name='add_comment'),
    path('payment/', views.payment_details, name='payment_details'),
    path('purchased-courses/', purchased_courses, name='purchased_courses'),
    path('buy-course/<int:course_id>/', buy_course, name='buy_course'),
     path('purchase/<int:course_id>/', views.purchase_course, name='purchase_course'),
     path('buy/<int:pk>',views.buy),
     path('my_payed',views.my_payed,name='my_payed')
    


]

