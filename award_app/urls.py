from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[

    url(r'^$',views.welcome, name='welcome'),
    url(r'^new/profileform$', views.my_profile, name='myprofile'),
    url(r'^new/profilepage$', views.profile_page, name='myprofilepage'),
    url(r'^new/project_image$', views.my_picture, name='project_image'),
    url(r'^new/project_image$', views.search_results, name='search_results'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
