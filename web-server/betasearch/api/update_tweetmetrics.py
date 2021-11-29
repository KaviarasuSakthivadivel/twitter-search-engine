import requests

from indexer import Indexer
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
        processed_docs=update_doc_withmetrics(docs)
        index_data(processed_docs)
        # with open('data/' + str(i) + '.json', 'w') as outfile:
        #     json.dump(docs, outfile)

def update_doc_withmetrics(docs):
    for doc in docs:
        tweet_id=doc['id']
        tweet=t.get_metrics(tweet_id)
        if tweet is not None:
            public_metrics=tweet.public_metrics
            doc['reply_count']=public_metrics['reply_count']
            doc['retweet_count']=public_metrics['retweet_count']
            doc['like_count']=public_metrics['like_count']
            doc['quote_count']=public_metrics['quote_count']
        else:
            doc['reply_count']=0
            doc['retweet_count']=0
            doc['like_count']=0
            doc['quote_count']=0
        
        
    return docs


def index_data(docs):
    # indexer.create_documents(processed_tweets)
    i.create_documents(docs)


if __name__ == '__main__':
    i = Indexer()
    t=Twitter()
    # i.do_initial_setup()
    # i.delete_fields()
    # i.add_fields()
    #download_data(core='IRF21P1_demo', aws_url='18.191.161.74', total_docs=179000)  # Kavi
    # download_data(core='IRF21P1', aws_url='18.217.75.107', total_docs=179000)  # Pak
    # download_data(core='IRF21P1', aws_url='18.223.120.151', total_docs=73000)  # Aashiq
    # download_data(core='IRF21P1', aws_url='3.136.97.247', total_docs=75000)  # Daya

    download_data(core='IRF21P1_demo', aws_url='3.15.218.16', total_docs=394000)  # entire corpus

    
