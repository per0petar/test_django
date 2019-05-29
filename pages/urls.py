from django.conf.urls import url, include

from . import views
from accounts.views import update_view
from music.views import library_view

app_name='pages'

urlpatterns = [
    url(r'^(?P<user_id>[0-9]+)/$', views.profile_view, name="profile"),
    # url(r'^other_users(?P<user_id>[0-9]+)/$', views.view_users, name="view_users"),
    url(r'^update/$', update_view, name="update_profile"),
]