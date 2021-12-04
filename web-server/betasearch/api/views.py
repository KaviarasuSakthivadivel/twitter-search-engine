import datetime
import time

import requests
from django.conf import settings
from django.http import JsonResponse
from rest_framework.decorators import api_view
import urllib.request
from googletrans import Translator

translator = Translator()


@api_view(['GET', 'POST'])
def search(request):
    if request.method == 'POST':
        start_time = time.time()
        query = request.data['query']
        pageNo = int(request.data['pageNo'])
        pageSize = int(request.data['pageSize'])
        poiName = None
        sentiment = None
        tweetLang = None
        country = None
        timestamp = None
        mentions = None
        show_only_replies = False
        show_only_poi = False
        showTweetsWithLinks = False
        replyCount = 0
        hashtags = None

        if request.data.get('poiName', None) is not None:
            poiName = list(request.data['poiName'])
            poiName = ' '.join(poiName)

        if request.data.get('sentiment', None) is not None:
            sentiment = list(request.data['sentiment'])
            sentiment = ' '.join(sentiment)

        if request.data.get('tweetLang', None) is not None:
            tweetLang = list(request.data['tweetLang'])
            tweetLang = ' '.join(tweetLang)

        if request.data.get('country', None) is not None:
            country = list(request.data['country'])
            country = ' '.join(country)

        if request.data.get('timestamp', None) is not None:
            timestamp = float(request.data['timestamp'])

        if request.data.get('mentions', None) is not None:
            mentions = str(request.data['mentions'])

        if request.data.get('showOnlyReplies', False) is not False:
            show_only_replies = bool(request.data['showOnlyReplies'])

        if request.data.get('showOnlyPoi', False) is not False:
            show_only_poi = bool(request.data['showOnlyPoi'])

        if request.data.get('showTweetsWithLinks', False) is not False:
            showTweetsWithLinks = bool(request.data['showTweetsWithLinks'])

        if request.data.get('replyCount', 0) != 0:
            replyCount = int(request.data['replyCount'])

        if request.data.get('hashtags', None) is not None:
            hashtags = str(request.data['hashtags'])
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
                "(" + query_es + ")" + " OR " + \
            "text_hi:" + "(" + query_hi + ")"
        q = urllib.parse.quote(query, encoding="UTF-8")

        # POI Name filter
        if poiName is not None:
            f_query = f_query + " AND " + "poi_name:" + "(" + poiName + ")"

        if sentiment is not None:
            f_query = f_query + " AND " + "sentiment:" + "(" + sentiment + ")"

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
            f_query = f_query + " AND " + "tweet_date:" + \
                "[" + tweetDate + " TO NOW" + "]"

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
        if replyCount != 0:
            f_query = f_query + " AND " + "reply_count:" + \
                "[" + str(replyCount) + "TO *" + "]"

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
            final_query += '&fq=' + \
                urllib.parse.quote(f_query, encoding="UTF-8")

        # Facet query formulations
        facet_json = {"facet": {"tweet_lang": {"type": "terms", "field": "tweet_lang", "limit": 20},
                                "poi_name": {"type": "terms", "field": "poi_name", "limit": 30},
                                "country": {"type": "terms", "field": "country", "limit": 10},
                                "hashtags": {"type": "terms", "field": "hashtags", "limit": 30}}}
        response = requests.get(final_query, json=facet_json)
        json_response = response.json()
        json_response['time_taken'] = str(
            round((time.time() - start_time), 2))+'s'
        return JsonResponse(json_response)


def get_replies(request, tweet_id):

    # method to get the replies for a tweet using tweet id invoked by /api/get_replies/tweet_id/"
    q = "replied_to_tweet_id:"+tweet_id
    q = urllib.parse.quote(q, encoding="UTF-8")

    reply_query = 'http://' + settings.AWS_URL + ':8983/solr/' + settings.CORE + '/query?q=' + \
        q
    response = requests.get(reply_query)
    json_response = response.json()
    return JsonResponse(json_response)
