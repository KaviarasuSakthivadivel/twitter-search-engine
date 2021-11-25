import requests
from django.conf import settings
from django.http import JsonResponse
from rest_framework.decorators import api_view
import urllib.request
from googletrans import Translator


translator = Translator()


@api_view(['GET', 'POST'])
def search(request):
    if request.method == 'GET':
        query = request.GET['query']
        pageNo = int(request.GET['pageNo'])
        pageSize = int(request.GET['pageSize'])
        if query is None:
            query = '*'
        start = (pageNo-1)*pageSize
        row = pageSize
        # translate the given query in all three languages(en,hi,es) to support search results in all three languages
        translator_en = translator.translate(query, dest='en')
        query_en = translator_en.text
        translator_es = translator.translate(query, dest='es')
        query_es = translator_es.text
        translator_hi = translator.translate(query, dest='hi')
        query_hi = translator_hi.text

        # query generation for text_en ,text_hi,text_es fields
        query = "text_en:"+"("+query+")^10"+" OR "+"text_es:"+"("+query+")^10"+" OR "+"text_hi:"+"("+query+")^10" + \
            "text_en:"+"("+query_en+")"+" OR "+"text_es:" + \
            "("+query_es+")"+" OR "+"text_hi:"+"("+query_hi+")"
        q = urllib.parse.quote(query, encoding="UTF-8")

        # hit Solr and get the docs with paination for each start and row combination
        response = requests.get('http://' + settings.AWS_URL + ':8983/solr/' + settings.CORE + '/query?q='
                                + q + '&start=' + str(start) + '&rows=' + str(row) + '&hl=true&hl.requireFieldMatch=false&hl.usePhraseHighLighter=false&hl.highlightMultiTerm=false&hl.fl=tweet_text')
        json_response = response.json()
        #results = json_response['response']
        # print(json_response)
        return JsonResponse(json_response)
