# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404

from accounts.models import User
from music.models import Album, Song
from music.forms import AlbumForm, SongForm


# Create your views here.


def home_page(request):
    query = request.GET.get('user')
    if query:
        users = User.objects.filter(full_name__icontains=query)
        return render(request, "home.html", {"users": users})
    else:
        return render(request, 'home.html')


def verify(request, uuid):
    try:
        user = User.objects.get(verification_uuid=uuid, is_verified=False, active = False)
    except User.DoesNotExist:
        raise Http404("User does not exist or is already verified")
 
    user.is_verified = True
    user.active = True
    user.save()
 
    return render(request, 'account_verified.html', {'user':user})


def profile_view(request, user_id):
    profile = get_object_or_404(User, id=user_id)
    query = request.GET.get('user')
    users = User.objects.all() #[:1]  Gets all users but limits the number shown with use of square brackets [] 

    if query:
        users = User.objects.filter(full_name__icontains=query)
        context = {
        'profile': profile,
        'users'  : users
        }
        return render(request, "pages/profile_home.html", context)
    else:
        context = {
        'profile': profile,
        'users'  : users
    }
    return render(request, "pages/profile_home.html", context)

# def view_users(request, user_id):
#     profile = get_object_or_404(User, id=user_id)
#     context = {
#         'profile': profile,
#         'users'  : users
#     }
#     return render(request, "pages/view_users.html", context)

# def download_handler(request, song_id):
#     song = get_object_or_404(Song, id=song_id)
#     filename = os.path.basename(Song.audio_file)
#     response = HttpResponse(Song.audio_file, content_type='text/plain')
#     response['Content-Disposition'] = 'attachment; filename=%s' % filename

#     return response

# users = User.objects.all()


# def other_user_view(request):
#     users = User.objects.all()

#     return render(request, 'pages/profile_home.html', {'users': users})
