from django.conf.urls import url, include

from . import views

app_name='music'

urlpatterns = [
    url(r'^my_library/(?P<user_id>[0-9]+)/$', views.library_view, name="my_library"),
    url(r'^my_library/(?P<user_id>[0-9]+)/(?P<filter_by>\w*.+)/$', views.library_view, name="my_library"),
    url(r'^upload_album/$', views.upload_album_view, name="upload_album"),
    url(r'^upload_song/(?P<album_id>[0-9]+)/$', views.upload_song_view, name="upload_song"),
    url(r'^detail/(?P<user_id>[0-9]+)/(?P<album_id>[0-9]+)/$', views.album_detail_view, name='album_detail'),
    url(r'^(?P<album_id>[0-9]+)/favorite/(?P<song_id>[0-9]+)/$', views.favorite_song, name='favorite_song'),
    url(r'^(?P<user_id>[0-9]+)/(?P<album_id>[0-9]+)/favorite_album/$', views.favorite_album, name='favorite_album'),
    url(r'^(?P<album_id>[0-9]+)/delete_song/(?P<song_id>[0-9]+)/$', views.delete_song, name='delete_song'),
    url(r'^(?P<album_id>[0-9]+)/delete_album/$', views.delete_album, name='delete_album'),
    url(r'^(?P<album_id>[0-9]+)/add_to_library/$', views.add_to_library, name='add_to_library')
    # url(r'^filter_by/(?P<user_id>[0-9]+)/(?P<filterby>\w+.+)/$', views.filters, name='filter_by'),
]