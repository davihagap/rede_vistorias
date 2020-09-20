from django.shortcuts import render
from django.http import HttpResponse

import json

from movies_api.service import get_ordered_movies


def getMoviesInOrder(request):
    
    if request.method != 'GET':
        return HttpResponse(json.dumps({'message': 'Method not allowed on this route'}), content_type='text/json', status=405)
    
    order = request.GET.get('order')
    if order == None:
        return HttpResponse(json.dumps({'message': 'Parms doens\'t match correct pattern (order parm required)'}), content_type='text/json', status=412)
    
    movies = get_ordered_movies(order)
    
    if len(movies) == 0:
        return HttpResponse(json.dumps({'message': 'Not found'}), content_type='text/json', status=404)
    
    return HttpResponse(json.dumps(movies), content_type='text/json', status=200)