from django import template
from posts.models import Post
register = template.Library()

@register.filter(name='liked')
def liked(user, post_id):
	post = Post.objects.get(pk=post_id)
	return user in post.likes.all()