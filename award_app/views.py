from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Profile,Projects
from .forms import ProfileForm,ProjectsForm
#ProjectsForm

# Create your views here.

def welcome(request):   
    return render(request,'welcome.html')

@login_required(login_url='/accounts/login/')
def profile_page(request):
    current_user = request.user
    img=Profile.objects.all()
    pic=Projects.objects.all()
    num_posts=Projects.objects.all().count()
    return render(request,'myprofile.html',{"img": img,"pic":pic,"num_posts":num_posts})


@login_required(login_url='/accounts/login/')
def my_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return redirect('myprofilepage')

    else:
        form = ProfileForm()
    return render(request, 'profile.html', {"form": form})

@login_required(login_url='/accounts/login/')
def my_picture(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProjectsForm(request.POST, request.FILES)
        if form.is_valid():
            picture = form.save(commit=False)
            picture.user = current_user
            picture.save()
        return redirect('myprofilepage')

    else:
        form = ProjectsForm()
    return render(request, 'pictures.html', {"form": form})

def search_results(request):

    if 'title' in request.GET and request.GET["title"]:
        search_term = request.GET.get("title")
        searched_images = Projects.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'registration/search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'registration/search.html',{"message":message})  