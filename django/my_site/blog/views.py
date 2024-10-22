from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
from .forms import CommentForm

from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
# Create your views here.


# def index(request):
#     latest_posts = Post.objects.all().order_by("-date")[:3]
#     return render(request, "blog/index.html", {
#         "posts": latest_posts
#     })

class IndexView(ListView):
    template_name = "blog/index.html"
    model = Post
    context_object_name = "posts"  # default: object_list
    ordering = ["-date"]

# setup queryset to return only last 3 articles
    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data


# def posts(request):
#     all_posts = Post.objects.all()
#     return render(request, "blog/all-posts.html", {
#         "all_posts": all_posts
#     })


class AllPostsView(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    context_object_name = "all_posts"
    ordering = ["-date"]


# def post_detail(request, slug):
#     # identified_post = Post.objects.get(slug=slug)
#     identified_post = get_object_or_404(Post, slug=slug)
#     return render(request, "blog/post-detail.html", {
#         "post": identified_post,
#         "post_tags": identified_post.tags.all()
#     })

# without comment form
# class SinglePostView(DetailView):
#     template_name = "blog/post-detail.html"
#     model = Post
#     context_object_name = "post"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["post_tags"] = self.object.tags.all()
#         return context

class SinglePostView(DetailView):
    template_name = "blog/post-detail.html"
    model = Post
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_tags"] = self.object.tags.all()
        context["comment_form"] = CommentForm()
        return context
