from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from tinymce.models import HTMLField


category_choices = (
    ('Undefined', 'UNDEFINED'),
    ('Sport', 'SPORT'),
    ('Art', 'ART'),
    ('Music', 'MUSIC'),
    ('Nature', 'NATURE'),
    ('Tech', 'TECH'),
    ('Culture', 'CULTURE'),
    ('Programming', 'PROGRAMMING'),
)
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = HTMLField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    review_star = models.IntegerField(default=0)
    category = models.CharField(max_length=20, choices=category_choices, default='Undefined')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    parent_comment = models.ForeignKey('self', related_name='children', null=True, on_delete=models.CASCADE)
    related_to_comment_id = models.IntegerField(default=0)
    title = models.CharField(max_length=50, default='')
    content = HTMLField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.content


class Review(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='reviews')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews_authors')
    review_star = models.IntegerField()

    def __str__(self):
        return f"{self.review_star} for Post ID {self.post.id} by {self.author}"
