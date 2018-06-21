from django.urls import path
from . import views
from django.contrib.auth.views import login, logout, password_reset, password_reset_done

urlpatterns = [
    path('admin/', views.admin, name='admin'),
    path('savecomment/', views.savecomment, name='savecomment'),
    path('index/', views.index, name='index'),
    path('base/', views.base, name='base'),
    path('political/', views.political, name='political'),
    path('contact/', views.contact, name='contact'),
    path('breaking/', views.breaking, name='breaking'),
    path('business/', views.business, name='business'),
    path('entertainment/', views.entertainment, name='entertainment'),
    path('events/', views.events, name='events'),
    path('health/', views.health, name='health'),
    path('lifestyle/', views.lifestyle, name='lifestyle'),
    path('shortcodes/', views.shortcodes, name='shortcodes'),
    path('single/', views.single, name='single'),
    path('sports/', views.sports, name='sports'),
    path('technology/', views.technology, name='technology'),
    path('videos/', views.videos, name='videos'),
    path('loginform/', views.loginform, name='loginform'),
    path('Admin/', views.Admn, name='Admn'),
    path('', login, {'template_name': 'website/login.html'}, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.UserFormView.as_view(), name='register'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit_profile/', views.edit_profile, name='edit_profile'),
    path('change_password/', views.change_password, name='change_password'),
    #path('reset_password/', views.reset_password, name='reset_password'),
   # path('reset_password/done/',views.password_reset_done, name='password_reset_done'),
]