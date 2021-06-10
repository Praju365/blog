
from django.urls import path
from users import views

urlpatterns = [
    path('register/' , views.UserCreateView.as_view() , name = 'user-register'),
    path('profile/' , views.profile, name = 'profile'),
]
