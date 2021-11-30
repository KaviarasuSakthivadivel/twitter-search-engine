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
        poiName = None
        tweetLang = None
        country = None
        timestamp = None
        mentions = None
        show_only_replies = False
        show_only_poi = False
        showTweetsWithLinks = False
        replyCount = 0
        hashtags = None
        if request.GET.get('poiName', None) is not None:
            poiName = str(request.GET['poiName'])

        if request.GET.get('tweetLang', None) is not None:
            tweetLang = str(request.GET['tweetLang'])

        if request.GET.get('country', None) is not None:
            country = str(request.GET['country'])

        if request.GET.get('timestamp', None) is not None:
            timestamp = float(request.GET['timestamp'])

        if request.GET.get('mentions', None) is not None:
            mentions = str(request.GET['mentions'])

        if request.GET.get('showOnlyReplies', False) is not False:
            show_only_replies = bool(request.GET['showOnlyReplies'])

        if request.GET.get('showOnlyPoi', False) is not False:
            show_only_poi = bool(request.GET['showOnlyPoi'])

        if request.GET.get('showTweetsWithLinks', False) is not False:
            showTweetsWithLinks = bool(request.GET['showTweetsWithLinks'])

        if request.GET.get('replyCount', 0) is not 0:
            replyCount = int(request.GET['replyCount'])

        if request.GET.get('hashtags', None) is not None:
            hashtags = str(request.GET['hashtags'])
        f_query = None
        if query is None:
            query = '*'
        if f_query is None:
            f_query = '*'
        start = (pageNo - 1) * pageSize
        row = pageSize

        # translate the given query in all three languages(en,hi,es) to support search results in all three languages
        translator_en = translator.translate(query, dest='en')
        query_en = translator_en.text
        translator_es = translator.translate(query, dest='es')
        query_es = translator_es.text
        translator_hi = translator.translate(query, dest='hi')
        query_hi = translator_hi.text

        # query generation for text_en ,text_hi,text_es fields
        query = "text_en:" + "(" + query + ")^10" + " OR " + "text_es:" + "(" + query + ")^10" + " OR " + "text_hi:" + "(" + query + ")^10" + \
                "text_en:" + "(" + query_en + ")" + " OR " + "text_es:" + \
                "(" + query_es + ")" + " OR " + "text_hi:" + "(" + query_hi + ")"
        q = urllib.parse.quote(query, encoding="UTF-8")

        # POI Name filter
        if poiName is not None:
            f_query = f_query + " AND " + "poi_name:" + "(" + poiName + ")"

        # Language filter
        if tweetLang is not None:
            f_query = f_query + " AND " + "tweet_lang:" + "(" + tweetLang + ")"

        # Country filter
        if country is not None:
            f_query = f_query + " AND " + "country:" + "(" + country + ")"

        # Created Time
        if timestamp is not None:
            timestamp = datetime.date.fromtimestamp(timestamp)
            tweetDate = timestamp.strftime("%Y-%m-%dT%H:%M:%SZ")
            f_query = f_query + " AND " + "tweet_date:" + "[" + tweetDate + " TO NOW" + "]"

        # mentions filter
        if mentions is not None:
            f_query = f_query + " AND " + "mentions:" + "(" + mentions + ")"

        # show only replies filter
        if show_only_replies is True:
            f_query = f_query + " AND " + "reply_text:" + "*"

        # show only poi tweets filter
        if show_only_poi is True:
            f_query = f_query + " AND " + "poi_name:" + "*"

        # show only tweets with replies filter
        if showTweetsWithLinks is True:
            f_query = f_query + " AND " + "tweet_text:" + "(http)"

        # minimum replies filter
        if replyCount is not 0:
            f_query = f_query + " AND " + "reply_count:" + "[" + str(replyCount) + "TO *" + "]"

        # hashtags filter
        if hashtags is not None:
            hashtags.replace("#", "")
            f_query = f_query + " AND " + "hashtags:" + "(" + hashtags + ")"

        # hit Solr and get the docs with pagination for each start and row combination
        final_query = 'http://' + settings.AWS_URL + ':8983/solr/' + settings.CORE + '/query?q=' + \
                      q + '&start=' + str(start) + '&rows=' + str(row) + \
                      '&hl=true&hl.requireFieldMatch=false&hl.usePhraseHighLighter=false&hl.highlightMultiTerm' \
                      '=false&hl.fl=tweet_text '
        if f_query is not None:
            final_query += '&fq=' + urllib.parse.quote(f_query, encoding="UTF-8")

        # Facet query formulations
        facet_json = {"facet": {"tweet_lang": {"type": "terms", "field": "tweet_lang", "limit": 20},
                                "poi_name": {"type": "terms", "field": "poi_name", "limit": 30},
                                "country": {"type": "terms", "field": "country", "limit": 10}}}
        response = requests.get(final_query, json=facet_json)
        json_response = response.json()
        print(json_response)
        return JsonResponse(json_response)
