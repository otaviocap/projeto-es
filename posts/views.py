from django.shortcuts import redirect, render
from django.contrib import messages

posts = [
	{
		"profile": {
			"name": "Dog Dog",
			"image": "/media/default.jpg"
		},
		"date": "1 min",
		"content": "AUAUAUAUAUAAUAUAUAUAUAUAUAUAUAUAU WOOF WOOF WOOF WOOF WOOF WOOF WOOF WOOF au au au au au au au au au au au au au auuuuuuuuu woof woof woof woof woof schlop schlop schlop schlop auauauauauauau woooooooooooooof woof woof woof AUAUAUAUAUAUAUAU",
		"likes":256,
		"comments":128
	},
	{
		"profile": {
			"name": "Dog Dog",
			"image": "/media/default.jpg"
		},
		"date": "1 min",
		"image": "/static/images/bg.jpeg",
		"content": "AUAUAUAUAUAAUAUAUAUAUAUAUAUAUAUAU WOOF WOOF WOOF WOOF WOOF WOOF WOOF WOOF au au au au au au au au au au au au au auuuuuuuuu woof woof woof woof woof schlop schlop schlop schlop auauauauauauau woooooooooooooof woof woof woof AUAUAUAUAUAUAUAU",
		"likes":256,
		"comments":128
	},
]

def home(request):
	messages.success(request, "yey")
	return render(request, 'posts/home.html', {"posts": posts})

def profile(request):
	messages.success(request, "yey")
	return render(request, 'posts/profile.html', {"posts": posts})

def notifications(request):
	messages.success(request, "yey")
	return render(request, 'posts/profile.html')