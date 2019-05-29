from django.conf.urls import url

from . import views

app_name = 'posts'

urlpatterns = [
    url(r'^$', views.view_posts, name="view_posts"),
    url(r'^create_post/$', views.post_create_view, name="create_post"),
    url(r'^(?P<post_id>[0-9]+)/$', views.detail_view, name="detail_view"),
];