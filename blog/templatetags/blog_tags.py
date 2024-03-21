from django import template
from ..models import Post

register = template.Library()

@register.inclusion_tag('blog/recent_posts.html')
def recent_posts(count=5):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}