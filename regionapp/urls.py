from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.landing, name='landing'),
    path('login/',views.signin,name='login'),
    path('register/',views.register,name='register'),
    path('logout/',views.signout,name='logout'),
    path('index/',views.index,name='index'),
    path('new-region/', views.create_region, name='new-region'),
    path('<region_id>/new-post/', views.create_post, name='post'),
    path('join_hood/<id>', views.join_hood, name='join-hood'),
    path('leave_hood/<id>', views.leave_hood, name='leave-hood'),
    path('all-hoods/', views.hoods, name='hood'),
    path('search/', views.search_business, name='search'),
    path('profile/<username>', views.profile, name='profile'),
    path('profile/<username>/edit/', views.edit_profile, name='edit-profile'),
    path('single_region/<region_id>', views.single_region, name='single-region'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)