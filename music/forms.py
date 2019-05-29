from django import forms

from music.models import Album, Song



class AlbumForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = ['artist', 'album_title', 'genre', 'album_logo']


class SongForm(forms.ModelForm):
    song_title = forms.CharField(label="Song Title", widget=forms.TextInput(attrs={'placeholder':'Title'}))
    # audio_file = forms.FileField(label="dddd", widget=placeholder="aaa")
    class Meta:
        model = Song
        fields = ['song_title', 'audio_file']
        # widgets = {
        #     'audio_file':forms.FileInput(attrs={'style':'display: none;',
        #                                      'class':'form-control', 
        #                                      'required': True, } 
        #                              )
        # }
        