import requests
import sys

from indexer import Indexer
from sentiment_analysis import analyze_sentiment
from twitter import Twitter


def download_data(core, aws_url, total_docs):
    count = 1000
    pages = int(total_docs / count)
    rows = count
    for i in range(pages):
        print(i)
        start = i * count
        response = requests.get('http://' + aws_url + ':8983/solr/' + core + '/query?q=*&start='
                                + str(start) + '&rows=' + str(rows))
        json_response = response.json()
        # print(json_response)
        docs = json_response['response']['docs']
        processed_docs = []
        for doc in docs:
            del doc['_version_']
            processed_docs.append(doc)
        index_data(processed_docs)
        # with open('data/' + str(i) + '.json', 'w') as outfile:
        #     json.dump(docs, outfile)


def do_sentiment_analysis(core, aws_url, total_docs):
    count = 1000
    pages = int(total_docs / count)
    rows = count
    for i in range(pages):
        # print(i)
        start = i * count
        response = requests.get('http://' + aws_url + ':8983/solr/' + core + '/query?q=*&start='
                                + str(start) + '&rows=' + str(rows))
        json_response = response.json()
        # print(json_response)
        docs = json_response['response']['docs']
        processed_docs = []
        for doc in docs:
            del doc['_version_']
            if doc['tweet_lang'] != 'hi' and 'sentiment' not in doc :
                sentiment, score, magnitude = analyze_sentiment(doc['tweet_text'], doc['tweet_lang'])
                print(score)
                print(magnitude)
                doc['sentiment'] = sentiment
                doc['doc_score'] = score
                doc['doc_magnitude'] = magnitude
                processed_docs.append(doc)
        if len(processed_docs) > 0:
            index_data(processed_docs)


def get_tweet_insights(core, aws_url, total_docs):
    count = 10
    pages = int(total_docs / count)
    rows = count
    for i in range(pages):
        print(i)
        start = i * count
        response = requests.get('http://' + aws_url + ':8983/solr/' + core + '/query?q=*&start='
                                + str(start) + '&rows=' + str(rows))
        json_response = response.json()
        docs = json_response['response']['docs']
        processed_docs = []
        for doc in docs:
            del doc['_version_']
            doc = update_doc_with_metrics(doc)
            processed_docs.append(doc)
        if len(processed_docs) > 0:
            print(processed_docs)
            index_data(processed_docs)


def update_doc_with_metrics(doc):
    tweet_id = doc['id']
    tweet = t.get_metrics(tweet_id)
    tweet_metrics = tweet[0]
    tweet_includes = tweet[1]
    if tweet_metrics is not None:
        public_metrics = tweet_metrics.public_metrics
        doc['reply_count'] = public_metrics['reply_count']
        doc['retweet_count'] = public_metrics['retweet_count']
        doc['like_count'] = public_metrics['like_count']
        doc['quote_count'] = public_metrics['quote_count']
    else:
        doc['reply_count'] = 0
        doc['retweet_count'] = 0
        doc['like_count'] = 0
        doc['quote_count'] = 0
    if tweet_includes is not None:
        doc['username'] = tweet_includes['users'][0].username
        doc['profile_name'] = tweet_includes['users'][0].name
        doc['profile_url'] = tweet_includes['users'][0].profile_image_url
        doc['verified'] = tweet_includes['users'][0].verified
    return doc


def index_data(docs):
    i.create_documents(docs)


if __name__ == '__main__':
    i = Indexer()
    t = Twitter()
    # i.do_initial_setup()
    # i.delete_fields()
    # i.add_fields()

    ################ Indexing from other solr instances #################
    # download_data(core='IRF21P1_demo', aws_url='18.191.161.74', total_docs=179000)  # Kavi
    # download_data(core='IRF21P1', aws_url='18.217.75.107', total_docs=179000)  # Pak
    # download_data(core='IRF21P1', aws_url='18.223.120.151', total_docs=73000)  # Aashiq
    # download_data(core='IRF21P1', aws_url='3.136.97.247', total_docs=75000)  # Daya

    ############### Sentiment analysis code from google API ############
    arguments = sys.argv
    type = arguments[1]
    if type == "1":
        print("coming in 1")
        do_sentiment_analysis(core='IRF21P1_demo', aws_url='3.20.12.127', total_docs=400000)  # Kavi
    else:
        print("coming in")
        get_tweet_insights(core='IRF21P1_demo', aws_url='3.20.12.127', total_docs=394000)  # entire corpus
