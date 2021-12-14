from django.shortcuts import HttpResponse
import json


def send_fail_http_response(msg=None):
    args = {}
    args['status'] = 'FAIL'
    args['response'] = msg
    the_data = json.dumps(args)
    response = HttpResponse(the_data, content_type='application/json', status=400)
    return response
