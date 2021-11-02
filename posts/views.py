from django.contrib.auth.models import User
from django.db.models.query import RawQuerySet
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages


from posts.models import Post

@login_required
def home(request):
	posts = Post.objects.filter(parent=None).order_by("date_posted").reverse()
	
	return render(request, 'social/home.html', {"posts": posts})

@login_required
def friends_home(request):
	posts = Post.objects.filter(parent=None, author__in=request.user.profile.following.all()).order_by("date_posted").reverse()

	if len(posts) == 0:
		messages.info(request, "Você ainda não tem amigos... Olhe na home principal e siga aqueles que te interessam")
	
	return render(request, 'social/home.html', {"posts": posts})

@login_required
def profile(request, username):
	user = User.objects.get(username=username)
	posts = Post.objects.filter(author=user).order_by("date_posted").reverse()

	return render(request, 'social/profile.html', {
		"profile_user": user,
		"posts": posts
	})

@login_required
def profile_without_user(request):
	return profile(request, username=request.user.username)

@login_required
def post(request):
	if request.method == "POST":
		post = Post(
			content=request.POST["post_text"],
			author=request.user
		)
		post.save()

	return render(request, 'goBack.html')

@login_required
def like(request, post_id):
	if request.method == "POST":
		post = get_object_or_404(Post, pk=post_id)
		if (request.user in post.likes.all()):
			post.likes.remove(request.user)
		else:
			post.likes.add(request.user)

		post.save()
	return render(request, 'goBack.html')

@login_required
def single_post(request, post_id):
	post = get_object_or_404(Post, pk=post_id)
	if request.method == "POST":
		post = Post(
			content=request.POST["post_text"],
			author=request.user,
			parent=post
		)
		post.save()
		return render(request, 'goBack.html')

	comments = Post.objects.filter(parent=post_id)

	return render(request, 'social/post.html', {"post": post, "posts":comments})