from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

from . import views
urlpatterns = [
   path('', views.index, name='index'),
   path('moviesingle/<int:id>/', views.moviesingle, name='moviesingle'),
   path('moviegrid/', views.moviegrid, name='moviegrid'),
   path('movielist/', views.movielist, name='movielist'),
   path('moviegridwf/', views.moviegridfw, name='moviegridwf'),
   path('seriessingle/', views.seriessing, name='seriessingle'),
   path('celebritysingl/', views.celebritygrid, name='celebritysingl'),
   path('celebritysingle1', views.celebritygrid1, name='celebritysingle1'),
   path('celebritysingle2/', views.celebritygrid02, name='celebritysingle2'),
   path('celebritylist/', views.celebritylist, name='celebritylist'),
   path('bloglist/', views.bloglist, name='bloglist'),
   path('bloggrid/', views.bloggrid, name='bloggrid'),
   path('userfavoritegrid/', views.userfavoritegrid, name='userfavoritegrid'),
   path('userfavoritelist/', views.userfavoritelist, name='userfavoritelist'),
   path('comingsoon/', views.comingsoon, name='comingsoon'),
   path('landing/', views.landing, name='landing'),
   path('userrate/', views.userrate, name='userrate'),
   path('userprofile/', views.userprofile, name='userprofile'),
   path('blogdetail/', views.blogdetail, name='blogdetail'),
   path('signup/', views.signuppage, name='signup'),
   path("login/", views.loginpage, name='login'),
   path('logout/', views.logoutuser, name='logout'),
   path('accounts/', include('allauth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)