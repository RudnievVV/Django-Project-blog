from django import template
from django.utils.html import mark_safe
from blog.models import Post


register = template.Library()


@register.simple_tag(name='latest_posts')
def latest_posts():
    latest_posts_html = ''
    latest_posts_list = Post.objects.all().order_by('-date_posted')[:3]
    for post in latest_posts_list:
        latest_posts_html += f"<br><a href='/post/{post.id}/'>{post.title}</a>"
    return mark_safe(latest_posts_html)
