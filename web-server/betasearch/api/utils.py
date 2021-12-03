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
    count = 100
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
        tweet_ids=[]
        for doc in docs:
            if 'profile_url' not in doc:
                del doc['_version_']
                tweet_ids.append(doc['id'])
                
        ids = ','.join(tweet_ids)
        
        processed_docs=update_doc_with_metrics(ids,docs)
        

        if len(processed_docs) > 0:
            index_data(processed_docs)


def update_doc_with_metrics(ids,docs):
    
    tweet_metrics = t.get_metrics(ids)
    for doc in docs:
        if doc['id'] in tweet_metrics:
            tweet_id=doc["id"]
            doc['reply_count'] = tweet_metrics[tweet_id]['reply_count']
            doc['retweet_count'] = tweet_metrics[tweet_id]['retweet_count']
            doc['like_count'] = tweet_metrics[tweet_id]['like_count']
            doc['quote_count'] = tweet_metrics[tweet_id]['quote_count']
            doc['username'] = tweet_metrics[tweet_id]["username"]
            doc['profile_name'] = tweet_metrics[tweet_id]["profile_name"]
            doc['profile_url'] = tweet_metrics[tweet_id]["profile_url"]
            doc['verified'] = tweet_metrics[tweet_id]["verified"]
        

    
    return docs


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
