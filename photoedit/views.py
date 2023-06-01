from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Course
from django.contrib.auth.decorators import login_required
from .models import Vlog
from .models import UserProfile
from .models import Tutorial
from django.shortcuts import redirect



def index(request):
    tutorials = Tutorial.objects.all()
    context = {'tutorials': tutorials}
    return render(request, 'index.html', context)


def tutorial(request, tutorial_id):
    return HttpResponse(f"You're looking at tutorial {tutorial_id}.")

def about(request):
    return render(request, 'photoedit/about.html')

def base(request):
    return render(request, 'base.html')

def sidebar(request):
    return render(request, 'sidebar.html')



def detail(request, tutorial_id):
    tutorial = get_object_or_404(Tutorial, pk=tutorial_id)
    context = {'tutorial': tutorial}
    return render(request, 'detail.html', context)














from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login
from django.contrib.auth import logout







from .models import UserSection

def login_view(request):
    tutorials = Tutorial.objects.all()
    context = {'tutorials': tutorials}

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # Create a new UserSection instance for the logged-in user
            user_section = UserSection.objects.create(user=user)
            # Pass the user_section object to the template
            context['user_section'] = user_section
            return render(request, 'index.html', context)

    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

from django.contrib.auth import logout


from django.contrib.auth import logout
from .models import UserSection

def logout_view(request):
    if request.user.is_authenticated:
        # Delete the UserSection instance for the logged-out user
        UserSection.objects.filter(user=request.user).delete()
        logout(request)
    return redirect("http://127.0.0.1:8000/login/")

# views.py

from django.contrib.auth import login
from .forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("http://127.0.0.1:8000/")
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})





# @login_required(login_url="http://127.0.0.1:8000/login/")

def software_list(request):
    courses = Course.objects.all()
    return render(request, 'software_list.html', {'courses': courses})




from .models import Course, Comment
from .forms import CommentForm

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    course_content = course.coursecontent_set.all()
    comments = Comment.objects.filter(course=course)

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.course = course
            comment.save()
            return redirect('course_detail', pk=pk)

    return render(request, 'course_detail.html', {
        'course': course,
        'course_content': course_content,
        'form': form,
        'comments': comments,
    })

def add_comment(request, pk):
    course = get_object_or_404(Course, pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.course = course
            comment.save()
            return redirect('photoedit:course_detail', pk=pk)

    return redirect('photoedit:course_detail', pk=pk)



   
from .models import PayedCourse

@login_required(login_url="http://127.0.0.1:8000/login/")
def p_course(request):
    courses = PayedCourse.objects.all()
    context = {'courses': courses}
    return render(request, 'p_course.html', context)



def about(requst):
    return render (requst,'about.html')


from .models import Course



from .models import PayedCourse, PCourseContent

def p_detail(request, pk):
    course = get_object_or_404(PayedCourse, pk=pk)
    course_content = course.course_content.all()
    user=request.user
    payed=pays.objects.filter(user=user,course=course)
    print(len(payed))
    if len(payed) > 0:
        f=1
    else:
        f=0
    print(f)
    return render(request, 'p_details.html', {'course': course, 'course_content': course_content,'pays':f})




from .models import PurchasedCourse

@login_required
def purchased_courses(request):
    user = request.user
    purchased_courses = PurchasedCourse.objects.filter(user=user)
    return render(request, 'purchased_courses.html', {'purchased_courses': purchased_courses})




# views.py
from .models import Course, MyCourse

@login_required(login_url="http://127.0.0.1:8000/login/")
def add_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    created = MyCourse.objects.get_or_create(user=request.user, course=course)
    if created:
        # The my course was created
        messages.success(request, f"{course.title} has been added to your courses.")
    else:
        # The my course already exists
        messages.warning(request, f"{course.title} is already in your courses.")
    return redirect("http://127.0.0.1:8000/my_courses/")

def courses(request):
    courses = Course.objects.all()
    return render(request, 'photoedit/courses.html', {'courses': courses})

@login_required(login_url="http://127.0.0.1:8000/login/")
def my_courses(request):
    my_courses = MyCourse.objects.filter(user=request.user)
    return render(request, 'my_courses.html', {'my_courses': my_courses})# views.py


def remove_course(request, my_course_id):
    my_course = get_object_or_404(MyCourse, id=my_course_id, user=request.user)
    my_course.delete()
    messages.success(request, f"{my_course.course.title} has been removed from your courses.")
    return redirect("http://127.0.0.1:8000/my_courses/")



def purchase_course(request, course_id):
    print(course_id)
    course = PayedCourse.objects.get(id=course_id)
   
    created = MyCourse.objects.create(user=request.user, course=course)
    created.save()
    if created:
        # The payed course was created
        messages.success(request, f"{course.title} has been added to your courses.")
    else:
        # The payed course already exists
        messages.warning(request, f"{course.title} is already in your courses.")
    return redirect("http://127.0.0.1:8000/my_courses/")



from .models import Tutorial

def search_view(request):
    query = request.GET.get('query')
    tutorials = Tutorial.objects.filter(title__icontains=query)
    context = {'tutorials': tutorials, 'query': query}
    return render(request, 'search.html', context)


from .models import Vlog

def blog(request):
    vlogs = Vlog.objects.all()  # Assuming you have a Vlog model to store vlog data

    context = {
        'vlogs': vlogs,
    }

    return render(request, 'blog.html', context)





from .forms import VlogForm

@login_required(login_url="http://127.0.0.1:8000/login/")
def add_vlog(request):
    if request.method == 'POST':
        form = VlogForm(request.POST, request.FILES)
        if form.is_valid():
            vlog = form.save(commit=False)
            vlog.user = request.user
            vlog.save()
            return redirect('http://127.0.0.1:8000/blog/')  # Replace 'home' with the URL name of the home page
    else:
        form = VlogForm()
    
    return render(request, 'add_vlog.html', {'form': form})



from django.http import JsonResponse

def delete_vlog(request, vlog_id):
    try:
        vlog = Vlog.objects.get(id=vlog_id)
    except Vlog.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Vlog not found.'}, status=404)
    
    # Check if the authenticated user is the owner of the vlog
    if vlog.user != request.user:
        return JsonResponse({'status': 'error', 'message': 'You are not authorized to delete this vlog.'}, status=403)

    vlog.delete()
    return JsonResponse({'status': 'success', 'message': 'Vlog deleted successfully.'})





def payment_details(request):
    if request.method == 'POST':
        # Handle form submission here
        # Process payment details and perform necessary actions
        pass
    else:
        return render(request, 'payment.html')



from .models import Course, PurchasedCourse


from .models import PayedCourse, UserProfile

from django.shortcuts import get_object_or_404

def buy_course(request, course_id):
    # Check if user is authenticated
    if request.user.is_authenticated:
        # Get the PayedCourse object
        course = get_object_or_404(PayedCourse, id=course_id)

        # Get or create the user profile
        user_profile, created = UserProfile.objects.get_or_create(user=request.user)

        # Check if the course is already purchased
        if course in user_profile.purchased_courses.all():
            return HttpResponse("You have already purchased this course.")

        # Add the course to the user's purchased courses
        user_profile.purchased_courses.add(course)

        # Redirect or return a response as needed
        return HttpResponse("Course purchased successfully.")
    else:
        return HttpResponse("You need to be logged in to purchase this course.")
    
from . models import pays 

def buy(request,pk):
    p=PayedCourse.objects.get(id=pk)
    user=request.user
    new=pays.objects.create(course=p,user=user)
    new.save()
    f=f"http://127.0.0.1:8000/p_details/{pk}"
    return redirect(f)


def my_payed(request):
    user=request.user
    my=pays.objects.filter(user=user)
    return render(request,'my_payed.html',{'my_courses': my})