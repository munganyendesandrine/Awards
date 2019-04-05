from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[

    # url(r'^$',views.welcome, name='welcome'),
    url(r'^$', views.profile_page, name='myprofilepage'),
    url(r'^new/profileform$', views.my_profile, name='myprofile'),
    url(r'^new/project_image$', views.my_picture, name='project_image'),
    url(r'^new/search$', views.search_results, name='search_results'),
    url(r'^new/rates$', views.my_rates, name='rates'),
    # url(r'^new/rates_like$', views.rates_like_dislike, name='rates_like'),
    url(r'^ajax/awards_profile/$', views.awards_profile, name='awards_profile'),
    url(r'^ajax/awards_projects/$', views.awards_projects, name='awards_projects'),
    url(r'^api/profile/$', views.ProfileList.as_view()),
    url(r'^api/projects/$', views.ProjectsList.as_view()),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
