from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    # path("", views.index, name="index"),
    path("admin/", views.login, name='login'),
    path("admin/logout", views.logout_request, name='logout'),
    path("admin/home/", views.home, name='home'),
    path("admin/profile", views.get_profile, name='get_profile'),


]