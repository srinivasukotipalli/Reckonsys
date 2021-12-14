from rest_framework.views import APIView
from django.http import JsonResponse
from Blog.blog_backend.models import Post


class GetAllPosts(APIView):
    def get(self, request, format=None):
        all_posts = list(Post.objects.values('id', 'title', 'description', 'publish_date', 'author'))
        return JsonResponse({"posts": all_posts})
