from django.urls import include, path, reverse_lazy
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
path('password_custom_change/',    
          auth_views.PasswordChangeView.as_view(
          template_name='registration/password_change.html', 
          success_url = reverse_lazy('password_change_custom_done')
          ),
          name='password_custom_change'
),
path('password_custom_change/done/', 
          auth_views.PasswordChangeDoneView.as_view(
          template_name='registration/password_change_custom_done.html', 
),          
name='password_change_custom_done'),

path("accounts/",include("django.contrib.auth.urls")),
path("dashboard/",views.dashboard, name='dashboard'),
path("signup/",views.signup, name='signup'),
]