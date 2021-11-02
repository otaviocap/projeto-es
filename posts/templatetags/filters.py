from django import template
from django.contrib.auth.models import User

from posts.models import Post
from posts.views import profile
register = template.Library()

@register.filter(name='liked')
def liked(user, post_id):
	post = Post.objects.get(pk=post_id)
	return user in post.likes.all()

@register.filter(name='following')
def following(user, username):
	profile_user = User.objects.get(username=username)
	logged_user = User.objects.get(username=user)

	return logged_user in profile_user.profile.followers.all()