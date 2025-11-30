from django.urls import path
from . import views

urlpatterns = [
    path('', views.home ,name="home"),
    path('login', views.login_func ,name="login"),
    path('signup', views.signup ,name="signup"),
    path('logout', views.logout ,name="logout"),
    path('change_name' ,views.change_name ,name="change_name"),
    path('create_post', views.create_post ,name="create_post"),
    path('profile', views.profile ,name="profile"),
    path('delete_task/<str:pk>', views.delete_task ,name="delete_task"),
    path('add_like/<str:post_id>' ,views.addLike ,name="addLike"),
]