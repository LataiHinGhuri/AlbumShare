from django.conf.urls import include,url
from . import views

app_name = 'app'

urlpatterns = [
    url(r'^$', views.HomeView, name='icon'),
    url(r'^home/$', views.HomeView, name='home'),
    url(r'^album/$', views.AlbumView, name='album'),
    url(r'^login/$', views.LogIn, name='login'),
    url(r'^register/$', views.Register, name='register'),
    url(r'^album/(?P<album_id>[0-9]+)/albumpassword/$',views.AlbumPasswordView, name='albumpassword'),
    url(r'^album/(?P<album_id>[0-9]+)/$', views.DetailView, name='detail'),
    url(r'^album/addalbum/$', views.AddAlbumView, name='addalbum'),
]
