from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Post
from django.views.generic import (ListView,
                                  CreateView,
                                  UpdateView,
                                  DetailView,
                                  DeleteView
                                  )
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy


# def home(request):
#     context = {
#         'posts': Post.objects.all()
#     }
#     return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # the default is '<app-name>/<model-name>_list.html'
    context_object_name = 'posts'  # the default is 'object_list'
    ordering = ['-date_posted']  # newest to oldest
    paginate_by = 6


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # the default is '<app-name>/<model-name>_list.html'
    context_object_name = 'posts'  # the default is 'object_list'
    paginate_by = 6

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'  # the default is 'object'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    # the default template of this view is "<app-name>/<model-name>_form.html"
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PostCreateView, self).form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    # the default template of this view is "<app-name>/<model-name>_form.html"
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PostUpdateView, self).form_valid(form)

    def test_func(self):
        post = self.get_object()
        return True if self.request.user == post.author else False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    # the default template of this view is "<app-name>/<model-name>_delete.html"
    success_url = reverse_lazy('home-blog')

    def test_func(self):
        post = self.get_object()
        return True if self.request.user == post.author else False


def about(request):
    return render(request, 'blog/about.html')
