from django.urls import path

from Blog.blog_backend.api.create_comment import CreateComment
from Blog.blog_backend.api.create_post import CreatePost
from Blog.blog_backend.api.delete_comment import DeleteComment
from Blog.blog_backend.api.get_all_posts import GetAllPosts
from Blog.blog_backend.api.get_post import GetPost
from Blog.blog_backend.api.update_post import UpdatePost

urlpatterns = [
    path("create_post/", CreatePost, name="create_post"),
    path("update_post/<int:post_id>/", UpdatePost, name="update_post"),
    path("create_comment/", CreateComment, name="create_comment"),
    path("delete_comment/<int:comment_id>/", DeleteComment, name="delete_comment"),
    path("get_posts/", GetAllPosts, name="get_posts"),
    path("get_post/<int:post_id>/", GetPost, name="get_post"),
]
