from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.views.generic.list import MultipleObjectMixin
from .models import Post, Comment
from .forms import CommentForm, CommentToCommentForm


def home(request):
    context = {'posts': Post.objects.all()}
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView, MultipleObjectMixin):
    model = Post
    paginate_by = 5

    def get_context_data(self, **kwargs):
        object_list = Post.objects.filter(id=self.get_object().id)[0].comments.filter(related_to_comment_id=0)
        context = super(PostDetailView, self).get_context_data(object_list=object_list, **kwargs)
        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user.profile.user
            comment.save()
            return redirect('post-detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})

@login_required
def add_comment_to_comment(request, pk, comm, comm_sub):
    post = get_object_or_404(Post, pk=pk)
    if comm_sub == 0:
        user = Post.objects.filter(id=pk)[0].comments.filter(id=comm)[0].author
        comment_title = Post.objects.filter(id=pk)[0].comments.filter(id=comm)[0].title
    else:
        user = Post.objects.filter(id=pk)[0].comments.filter(id=comm_sub)[0].author
        comment_title = Post.objects.filter(id=pk)[0].comments.filter(id=comm_sub)[0].title
    if request.method == "POST":
        form = CommentToCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user.profile.user
            comment.related_to_comment_id = comm
            comment.parent_comment = Post.objects.filter(id=pk)[0].comments.filter(id=comm_sub)[0]
            comment.save()
            return redirect('post-detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_comment.html', {'form': form, 'user': user, 'comment_title': comment_title})

@login_required
def remove_comment(request, pk, comm):
    post = get_object_or_404(Post, pk=pk)
    comment = get_object_or_404(Comment, id=comm)
    if request.method == "POST":
        comment.delete()
        messages.success(request, f'Your comment has been removed!')
        return redirect('post-detail', pk=post.pk)
    if request.user == comment.author:
        return render(request, 'blog/comment_confirm_delete.html', {'comment': comment})
    else:
        return redirect('post-detail', pk=post.pk)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
