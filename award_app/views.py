from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Profile,Projects,Rating2
from .forms import ProfileForm,ProjectsForm,RatingForm
from django.http import JsonResponse
#.............
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer,ProjectsSerializer
from rest_framework import status
from .permissions import IsAdminOrReadOnly


class ProfileList(APIView):
    
    def get(self, request, format=None):
        all_profile = Profile.objects.all()
        serializers = ProfileSerializer(all_profile, many=True)
        return Response(serializers.data)
        
    def post(self, request, format=None):
        serializers = ProfileSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        permission_classes = (IsAdminOrReadOnly,)


class ProjectsList(APIView):
    
    def get(self, request, format=None):
        all_projects = Projects.objects.all()
        serializers = ProjectsSerializer(all_projects, many=True)
        return Response(serializers.data)
        
    def post(self, request, format=None):
        serializers = ProjectsSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        permission_classes = (IsAdminOrReadOnly,)

# Create your views here.

# def welcome(request):   
#     return render(request,'welcome.html')

@login_required(login_url='/accounts/login/')
def profile_page(request):
    current_user = request.user
    img=Profile.objects.all()
    pic=Projects.objects.all()
    num_posts=Projects.objects.all().count()
    rating=Rating2.objects.all()
    return render(request,'myprofile.html',{"img": img,"pic":pic,"num_posts":num_posts,"rating":rating})


# @login_required(login_url='/accounts/login/')
# def rates_like_dislike(request):
#     rates=[1,2,3,4,5,6,7,8,9,10]
#     like=0
#     for i in rates:
#       like=like+1
#     return like
#     liked=Rating2.objects.all()
#     return render(request,'myprofile.html',{"liked":like})

# def index(request):
#     return render(request,'myprofile.html')
#----------------------------------
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


def awards_profile(request):
    user = request.POST.get('user')
    username = request.POST.get('username')
    profile_photo = request.POST.get('profile_photo')
    bio = request.POST.get('bio')
    contacts = request.POST.get('contacts')

    recipient = Profile(user=user, username=username, profile_photo=profile_photo, bio=bio, contacts=contacts)
    recipient.save()
    send_msg(user, username, profile_photo, bio, contacts)
    data = {'success': 'You have been successfully able to get the message'}
    return JsonResponse(data)

def awards_projects(request):
    title = request.POST.get('title')
    detailed_description = request.POST.get('detailed_description')
    link_to_livesite = request.POST.get('link_to_livesite')
    image_landing_page = request.POST.get('image_landing_page')
    recipient = Projects(title=title, detailed_description=detailed_description, link_to_livesite=link_to_livesite,image_landing_page=image_landing_page)
    recipient.save()
    send_msg(title, detailed_description, link_to_livesite, image_landing_page)
    data = {'success': 'You have been successfully able to get the message'}
    return JsonResponse(data)
#----------------------------------
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
        images = Projects.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'registration/search.html',{"message":message,"images":images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'registration/search.html',{"message":message})  

@login_required(login_url='/accounts/login/')
def my_rates(request):
    current_user = request.user
    if request.method == 'POST':
        form = RatingForm(request.POST, request.FILES)
        if form.is_valid():
            rates = form.save(commit=False)
            rates.user = current_user
            rates.save()
        return redirect('myprofilepage')

    else:
       form = RatingForm()
    return render(request, 'rates.html', {"form": form})