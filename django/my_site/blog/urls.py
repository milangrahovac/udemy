from django.urls import path
from . import views

# urlpatterns = [
#     path("", views.index, name="index"),
#     path("posts", views.posts, name="posts-page"),
#     path("posts/<slug:slug>", views.post_detail, name="post-detail-page")
# ]

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("posts", views.AllPostsView.as_view(), name="posts-page"),
    path("posts/<slug:slug>", views.SinglePostView.as_view(),
         name="post-detail-page"),
    path("read-later", views.ReadLaterView.as_view(), name="read-later")
]
