from django import template
from django.utils.html import mark_safe
from blog.models import Post


register = template.Library()


@register.simple_tag(name='latest_posts')
def latest_posts():
    latest_posts_html = ''
    latest_posts_list = Post.objects.all().order_by('-date_posted')[:3]
    for post in latest_posts_list:
        latest_posts_html += f"""<p><a href='/post/{post.id}/'>{post.title}</a>
                             <br><small class='text-muted'>Posted by <strong>{post.author}</strong></small></p>"""
    return mark_safe(latest_posts_html)


@register.filter
def user_post_review_check(user_reviews, post_id):
    if len(user_reviews.filter(post_id=post_id)):
        return True


