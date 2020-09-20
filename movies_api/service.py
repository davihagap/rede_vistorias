from movies_api.models import Movie, Sequence, PositionInOrder
from datetime import date

def beautify_result(res):
    result = []
    for r in res:
        temp_dict = {}
        for key, value in r.items():
            if type(value) is date:
                value = value.strftime('%Y-%m-%d')
            temp_dict[key[key.find('__') + 2:]] = value
        result.append(temp_dict)
    
    return result

def get_ordered_movies(order):
    res = PositionInOrder.objects.select_related('movie', 'sequence').filter(sequence__name=order).order_by('position').values('movie__title','movie__episode_id','movie__opening_crawl','movie__director','movie__producer','movie__release_date')
           
    return beautify_result(res)
