from rest_framework.views import APIView
from django.http import JsonResponse

from Blog.blog_backend.dispatchers.responses.send_fail_http_response import send_fail_http_response
from Blog.blog_backend.models import Post


class GetPost(APIView):
    def get(self, request, format=None):
        post_details = Post.objects.filter(pk=request.GET['id']).values(
            'id', 'title', 'description', 'publish_date', 'author').first()
        return JsonResponse({"post_details": post_details})
