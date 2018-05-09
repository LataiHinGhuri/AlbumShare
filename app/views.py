from django.views import generic
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Album, LoginControl
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from PIL import Image




def HomeView(request):
	all_albums = Album.objects.all()
	log_control = LoginControl.objects.get(pk=1)
	context = {'all_albums':all_albums,'log_control':log_control}
	return render(request,'app/home.html',context)

def AlbumView(request):
	log_control = LoginControl.objects.get(pk=1)
	
	if (request.method == "POST"):
		search_user = request.POST['search_user']
		all_albums = Album.objects.filter(owner=search_user)
		context = {'all_albums':all_albums,'log_control':log_control}
		return render(request,'app/albums.html',context)
	else:
		all_albums = Album.objects.all()
		context = {'all_albums':all_albums,'log_control':log_control}
		return render(request,'app/albums.html',context)

def AlbumPasswordView(request, album_id):
	log_control = LoginControl.objects.get(pk=1)
	if log_control.logtext=='login':
		return redirect('app:login') 
	else:
		all_albums = Album.objects.all()
		context = {'album_id':album_id,'log_control':log_control}
		return render(request,'app/album_password.html',context)



def DetailView(request,album_id):
	log_control = LoginControl.objects.get(pk=1)
	if log_control.logtext=='login':
		return redirect('app:login') 
	else:
		all_albums = Album.objects.all()
		album = Album.objects.get(pk=album_id)
		if 'album-password' in request.POST.keys():
			album_pass = request.POST['album-password']
		else:
			album_pass = album.password
		
		first_photo = album.photo_set.get(counter=0)
		album_photos = album.photo_set.all()[1:]
		if 'comment' in request.POST.keys():
			cmnt = request.POST['comment']
			if cmnt != 'write a comment':
				album.comments_set.create(user=request.user.username, comment= cmnt)
				album.save()
		album_comment = album.comments_set.all()
		context = {'all_albums':all_albums, 'album':album,'album_id':album_id, 
					'album_photos':album_photos, 'first_photo':first_photo, 
					'album_comment': album_comment, 'log_control':log_control}
		

		if album_pass == album.password:
			return render(request, 'app/details.html', context)
		else:
			messages.error(request, 'Please enter correct password...')
			return render(request, 'app/album_password.html', context)

		
def AddAlbumView(request):
	log_control = LoginControl.objects.get(pk=1)
	if(request.method=='POST'):
		album_title=request.POST['album_title']
		album_message=request.POST['album_message']
		album_password=request.POST['album_password']
		album_owner = request.user.username
		new_obj=Album.objects.create(album_title=album_title,album_message=album_message,password=album_password,owner=album_owner)
		images =request.FILES.getlist('photos')
		value=0
		for image in images:
			
			im = Image.open(image)
			width, height = im.size
			if height > 600:
				wpercent = (width/float(height))
				width = int((float(600)*float(wpercent)))
				height= 600

			fs = FileSystemStorage()
			filename = fs.save(image.name, image)

			imgurl=fs.url(filename)
			new_obj.photo_set.create(images=imgurl, counter=value, height=height,width=width )
			value=value+1
		
		new_obj.save()
		first_photo = new_obj.photo_set.get(counter=0)
		album_photos = new_obj.photo_set.all()[1:]
		album_comment = new_obj.comments_set.all()
		context = {'album_id':new_obj.pk, 'album':new_obj, 'album_photos':album_photos,
		 			'first_photo':first_photo, 'album_comment': album_comment,
		 			'log_control':log_control}
		return render(request, 'app/details.html',context)
	else:
		all_albums = Album.objects.all()
		if log_control.logtext=='login':
			return redirect('app:login')
		else:
			context = {'all_albums':all_albums,'log_control':log_control}
			return render(request,'app/add_album.html',context)


def LogIn(request):
	if(request.method=='POST'):
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request,user)
				lc=LoginControl.objects.get(pk=1)
				lc.logtext='logout'
				lc.profile=username
				lc.save()
				return redirect('app:home')
			else:
				context={'error':'incorrect'}
				return render(request,'app/login.html',context)
		else:
			context={'error':'incorrect'}
			return render(request,'app/login.html',context)

	else:
		lc=LoginControl.objects.get(pk=1)
		
		if lc.logtext=='login':
			context ={'error':'null'}
			return render(request,'app/login.html',context)
		else:
			lc.logtext='login'
			lc.profile='My Profile'
			lc.save()
			logout(request)
			context ={'error':'null'}
			return redirect('app:home')

def Register(request):

	if(request.method=='POST'):
		first_name = request.POST['firstname']
		last_name = request.POST['lastname']
		email = request.POST['email']
		username = request.POST['username']
		password = request.POST['password']
		confirm_password = request.POST['confirm_password']
		all_user = User.objects.all()
		for user in all_user:
			if user.username == username:
				context = {
					'error':'user',
					'name' :username
				}
				return render(request, 'app/register.html', context)

		if password == confirm_password:	
			user = User()
			user.username = username
			user.set_password(password)
			user.email = email
			user.first_name =first_name
			user.last_name= last_name
			user.save()
			return redirect('app:login')
		else:
			context = {
				'error':'mismatched'
			}
			return render(request, 'app/register.html', context)

	else:
		context = {
			'error':'null'
			}
		return render(request,'app/register.html',context)
