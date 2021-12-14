from django.shortcuts import HttpResponse
import json


def send_pass_http_response(msg=None):
    args = {}
    args['status'] = 'PASS'
    args['response'] = msg
    the_data = json.dumps(args)
    response = HttpResponse(the_data, content_type='application/json', status=200)
    return response
