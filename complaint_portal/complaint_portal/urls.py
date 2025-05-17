from django.contrib import admin#  Django's built-in admin panel.
from django.urls import path, include  # used to define path 
from users import views as user_views #Imports views from the users app.
from django.contrib.auth import views as auth_views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('complaints.urls')),
    path('register/', user_views.register, name='register'), #url path (prompts)
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html', next_page='login'), name='logout'),
    path('profile/', user_views.profile, name='profile'),
]# every pages link is connected 
#routing user when clicks url user enters new page using interation with django 
#User visits a URL → Django checks urlpatterns.
#If the URL matches a pattern, Django calls the corresponding view.
#The view returns a response (HTML page, JSON, etc.).

