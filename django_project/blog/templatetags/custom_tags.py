from django import template
from django.utils.html import mark_safe
from blog.models import Post, category_choices


register = template.Library()


@register.simple_tag
def latest_posts():
    latest_posts_html = ''
    latest_posts_list = Post.objects.all().order_by('-date_posted')[:3]
    for post in latest_posts_list:
        latest_posts_html += f"""<p><a href='/post/{post.id}/'>{post.title}</a>
                             <br><small class='text-muted'>Category: <strong>{post.category}</strong></small>
                             <br><small class='text-muted'>Posted by <strong>{post.author}</strong></small></p>"""
    return mark_safe(latest_posts_html)


@register.simple_tag
def category_list():
    category_list_html = ''
    for category_choice in category_choices:
        if len(Post.objects.filter(category=category_choice[0])):
            category_list_html += f"<a href='/category/{category_choice[0]}'>{category_choice[0]}</a>"
    return mark_safe(category_list_html)


@register.filter
def user_post_review_check(user_reviews, post_id):
    if len(user_reviews.filter(post_id=post_id)):
        return True


