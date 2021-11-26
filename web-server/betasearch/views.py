import requests
from django.conf import settings
from django.http import JsonResponse
from rest_framework.decorators import api_view
import urllib.request
from googletrans import Translator
import datetime 


translator = Translator()


@api_view(['GET', 'POST'])
def search(request):
    if request.method == 'GET':
        query = request.GET['query']
        pageNo = int(request.GET['pageNo'])
        pageSize = int(request.GET['pageSize'])
        poiName = str(request.GET['poiName'])
        tweetLang = str(request.GET['tweetLang'])
        country = str(request.GET['country'])
        timestamp = float(request.GET['timestamp'])
        mentions = str(request.GET['mentions'])
        showOnlyReplies = bool(request.GET['showOnlyReplies'])
        showOnlyPoi = bool(request.GET['showOnlyPoi'])
        showTweetsWithLinks = bool(request.GET['showTweetsWithLinks'])
        replyCount = int(request.GET['replyCount'])
        hashtags = str(request.GET['hashtags'])
        fQuery = None
        if query is None:
            query = '*'
        if fQuery is None:
            fQuery = '*'
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
        
        # POI Name filter
        if poiName is not None:
            fQuery = fQuery + " AND "+"poi_name:"+"("+poiName+")"

        # Language filter
        if tweetLang is not None:
            fQuery = fQuery + " AND "+"tweet_lang:"+"("+tweetLang+")"

        # Country filter
        if country is not None:
            fQuery = fQuery + " AND "+"country:"+"("+country+")"

        # Created Time
        if timestamp is not None:
            timestamp = datetime.date.fromtimestamp(timestamp)
            tweetDate = timestamp.strftime("%Y-%m-%dT%H:%M:%SZ")
            fQuery = fQuery + " AND "+"tweet_date:"+"["+tweetDate+" TO NOW"+"]"

        # mentions filter
        if mentions is not None:
            fQuery = fQuery + " AND "+"mentions:"+"("+mentions+")"

        # show only replies filter
        if showOnlyReplies is True:
            fQuery = fQuery + " AND "+"reply_text:"+"*"

        # show only poi tweets filter
        if showOnlyPoi is True:
            fQuery = fQuery + " AND "+"poi_name:"+"*"

        # show only tweets with replies filter
        if showTweetsWithLinks is True:
            fQuery = fQuery + " AND "+"tweet_text:"+"(http)"

        # minimum replies filter
        if replyCount is not None:
            fQuery = fQuery + " AND "+"reply_count:"+"["+replyCount+"TO *"+"]"

        # hashtags filter
        if hashtags is not None:
            hashtags.replace("#","")
            fQuery = fQuery + " AND "+"hashtags:"+"("+hashtags+")"

        # appending fq
        if fQuery is not None:
            fq = urllib.parse.quote(fQuery, encoding="UTF-8")
            finalQuery = 'http://' + settings.AWS_URL + ':8983/solr/' + settings.CORE + '/query?q=' + \
                        q + '&fq=' + fq + '&start=' + str(start) + '&rows=' + str(row) + \
                        '&hl=true&hl.requireFieldMatch=false&hl.usePhraseHighLighter=false&hl.highlightMultiTerm=false&hl.fl=tweet_text'
                        
        # hit Solr and get the docs with paination for each start and row combination
        finalQuery = 'http://' + settings.AWS_URL + ':8983/solr/' + settings.CORE + '/query?q=' + \
                    q + '&start=' + str(start) + '&rows=' + str(row) + \
                    '&hl=true&hl.requireFieldMatch=false&hl.usePhraseHighLighter=false&hl.highlightMultiTerm=false&hl.fl=tweet_text'

        response = requests.get(finalQuery)
        json_response = response.json()
        #results = json_response['response']
        # print(json_response)
        return JsonResponse(json_response)
