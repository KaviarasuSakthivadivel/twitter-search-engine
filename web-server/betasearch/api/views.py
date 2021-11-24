import requests
from django.conf import settings
from django.http import JsonResponse
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def search(request):
    if request.method == 'GET':
        query = request.GET['query']
        start = request.GET['start']
        offset = 10
        if query is None:
            query = '*'
        if start is None:
            start = 0
        response = requests.get('http://' + settings.AWS_URL + ':8983/solr/' + settings.CORE + '/query?q='
                                + query + '&start=' + str(start) + '&rows=' + str(offset))
        json_response = response.json()
        print(json_response)
        return JsonResponse(json_response, safe=False)

