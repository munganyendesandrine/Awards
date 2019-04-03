from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Profile,Projects
from .forms import ProfileForm,ProjectsForm
from django.http import JsonResponse
#.............
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer

#........
class MerchList(APIView):
    def get(self, request, format=None):
        all_merch = Profile.objects.all()
        serializers = ProfileSerializer(all_merch, many=True)
        return Response(serializers.data)

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


# @login_required(login_url='/accounts/login/')
# def my_profile(request):
#     current_user = request.user
#     if request.method == 'POST':
#         form = ProfileForm(request.POST, request.FILES)
#         if form.is_valid():
#             profile = form.save(commit=False)
#             profile.user = current_user
#             profile.save()
#         return redirect('myprofilepage')

#     else:
#         form = ProfileForm()
#     return render(request, 'profile.html', {"form": form})

#----------------------------------
@login_required(login_url='/accounts/login/')
def my_profile(request):
    current_user = request.user
    # if request.method == 'POST':
    #     form = ProfileForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         profile = form.save(commit=False)
    #         profile.user = current_user
    #         profile.save()
    #     return redirect('myprofilepage')

    # else:
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

