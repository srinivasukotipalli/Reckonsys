from django.http import JsonResponse
from rest_framework.views import APIView
# from rest_framework import authentication, permissions
from Blog.blog_backend.dispatchers.responses.send_fail_http_response import send_fail_http_response
from Blog.blog_backend.models import Post, Comment


class CreateComment(APIView):
    def post(self, request):
        post_id = request.POST.get('post_id')
        text = request.POST.get('text')
        author = request.POST.get('author')

        try:
            post = Post.objects.get(pk=post_id)
        except 'DoesNotExist':
            return send_fail_http_response(msg='Post Id does not exist')

        if text and author:
            comment = Comment.objects.create(post=post, text=text, author=author)
        else:
            return send_fail_http_response(msg='Please send all the required details')

        return JsonResponse({"comment": comment.id})
