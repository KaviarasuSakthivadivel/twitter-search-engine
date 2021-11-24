import requests

from indexer import Indexer


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


def index_data(docs):
    # indexer.create_documents(processed_tweets)
    i.create_documents(docs)


if __name__ == '__main__':
    i = Indexer()
    # i.do_initial_setup()
    # i.delete_fields()
    # i.add_fields()
    download_data(core='IRF21P1_demo', aws_url='18.191.161.74', total_docs=179000)  # Kavi
    # download_data(core='IRF21P1', aws_url='18.217.75.107', total_docs=179000)  # Pak
    # download_data(core='IRF21P1', aws_url='18.223.120.151', total_docs=73000)  # Aashiq
    # download_data(core='IRF21P1', aws_url='3.136.97.247', total_docs=75000)  # Daya
