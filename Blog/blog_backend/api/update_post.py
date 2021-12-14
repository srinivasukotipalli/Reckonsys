from rest_framework.views import APIView
from Blog.blog_backend.dispatchers.responses.send_fail_http_response import send_fail_http_response
from Blog.blog_backend.dispatchers.responses.send_pass_http_response import send_pass_http_response
from Blog.blog_backend.models import Post


class UpdatePost(APIView):
    def patch(self, request, post_id):
        post = Post.objects.filter(pk=post_id).first()

        title = request.POST.get('title')
        description = request.POST.get('description')
        author = request.POST.get('author')

        if post:
            if title:
                post.title = title
            if description:
                post.description = description
            if author:
                post.author = author
            post.save()
        else:
            return send_fail_http_response(msg='Post Id Does Not Exist')

        return send_pass_http_response(msg='Updated Successfully!')