from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.contrib import messages

from posts.models import Post

# posts = [
# 	{
# 		"profile": {
# 			"name": "Dog Dog",
# 			"image": "/media/default.jpg"
# 		},
# 		"date": "1 min",
# 		"content": "AUAUAUAUAUAAUAUAUAUAUAUAUAUAUAUAU WOOF WOOF WOOF WOOF WOOF WOOF WOOF WOOF au au au au au au au au au au au au au auuuuuuuuu woof woof woof woof woof schlop schlop schlop schlop auauauauauauau woooooooooooooof woof woof woof AUAUAUAUAUAUAUAU",
# 		"likes":256,
# 		"comments":128
# 	},
# 	{
# 		"profile": {
# 			"name": "Dog Dog",
# 			"image": "/media/default.jpg"
# 		},
# 		"date": "1 min",
# 		"image": "/static/images/bg.jpeg",
# 		"content": "AUAUAUAUAUAAUAUAUAUAUAUAUAUAUAUAU WOOF WOOF WOOF WOOF WOOF WOOF WOOF WOOF au au au au au au au au au au au au au auuuuuuuuu woof woof woof woof woof schlop schlop schlop schlop auauauauauauau woooooooooooooof woof woof woof AUAUAUAUAUAUAUAU",
# 		"likes":256,
# 		"comments":128
# 	},
# ]

def home(request):
	posts = Post.objects.all().order_by("date_posted").reverse()
	
	return render(request, 'posts/home.html', {"posts": posts})

def profile(request, username):
	user = User.objects.get(username=username)
	posts = Post.objects.filter(author=user).order_by("date_posted").reverse()

	return render(request, 'posts/profile.html', {
		"username": user,
		"posts": posts
	})

def profile_without_user(request):
	return profile(request, username=request.user.username)

def post(request):
	if request.method == "POST":
		post = Post(
			content=request.POST["post_text"],
			author=request.user
		)
		post.save()

	return render(request, 'goBack.html')

def like(request, post_id):
	if request.method == "POST":
		post = Post.objects.get(pk=post_id)
		if (request.user in post.likes.all()):
			post.likes.remove(request.user)
		else:
			post.likes.add(request.user)

		post.save()
	return render(request, 'goBack.html')


def notifications(request):
	messages.success(request, "yey")
	return render(request, 'posts/profile.html')