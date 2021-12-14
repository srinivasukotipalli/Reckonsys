from django.http import JsonResponse
from rest_framework.views import APIView
# from rest_framework import authentication, permissions
from Blog.blog_backend.dispatchers.responses.send_fail_http_response import send_fail_http_response
from Blog.blog_backend.models import Post


class CreatePost(APIView):
    # To Handle Token
    # authentication_classes = (authentication.TokenAuthentication,)
    # permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        title = request.POST.get('title')
        description = request.POST.get('description')
        author = request.POST.get('author')

        if title and description and author:
            post = Post.objects.create(
                title=title,
                description=description,
                author=author
            )
        else:
            send_fail_http_response(msg='Please Give me all the required details')
        return JsonResponse({"id": post.id})
