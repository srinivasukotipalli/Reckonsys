from rest_framework.views import APIView
from Blog.blog_backend.dispatchers.responses.send_fail_http_response import send_fail_http_response
from Blog.blog_backend.dispatchers.responses.send_pass_http_response import send_pass_http_response
from Blog.blog_backend.models import Comment


class DeleteComment(APIView):
    def delete(self, request, comment_id):
        try:
            comment = Comment.objects.get(pk=comment_id)
        except 'DoesNotExist':
            return send_fail_http_response(msg='Comment Id does not exist to delete')
        comment.delete()
        return send_pass_http_response(msg='Deleted Successfully!')
