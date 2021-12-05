import requests
from google.cloud import language_v1


def analyze_sentiment(text_content, language="en"):
    client = language_v1.LanguageServiceClient()

    # Available types: PLAIN_TEXT, HTML
    type_ = language_v1.Document.Type.PLAIN_TEXT

    # Optional. If not specified, the language is automatically detected.
    # For list of supported languages:
    # https://cloud.google.com/natural-language/docs/languages

    document = {"content": text_content, "type_": type_, "language": language}

    # Available values: NONE, UTF8, UTF16, UTF32
    encoding_type = language_v1.EncodingType.UTF8

    response = client.analyze_sentiment(request = {'document': document, 'encoding_type': encoding_type})
    # Get overall sentiment of the input document

    score = response.document_sentiment.score
    sentiment = 'neutral'
    if 0.15 < score < 2:
        sentiment = 'positive'
    elif score < -0.15:
        sentiment = 'negative'

    print(u"Document sentiment score: {}".format(response.document_sentiment.score))
    print(
        u"Document sentiment magnitude: {}".format(
            response.document_sentiment.magnitude
        )
    )
    # # Get sentiment for all sentences in the document
    # for sentence in response.sentences:
    #     print(u"Sentence text: {}".format(sentence.text.content))
    #     print(u"Sentence sentiment score: {}".format(sentence.sentiment.score))
    #     print(u"Sentence sentiment magnitude: {}".format(sentence.sentiment.magnitude))

    # Get the language of the text, which will be the same as
    # the language specified in the request or, if not specified,
    # the automatically-detected language.
    # print(u"Language of the text: {}".format(response.language))
    print("Overall sentiment:: " + sentiment)
    return sentiment, round(response.document_sentiment.score, 2), round(response.document_sentiment.magnitude,2)


def analyse_sentiment_deep_ai(text_content):
    sentiment = "neutral"
    score = 0.1
    magnitude = 1.8
    r = requests.post(
        "https://api.deepai.org/api/sentiment-analysis",
        data={
            'text': text_content,
        },
        headers={'api-key': '05a645ab-93e7-49a9-82ec-4f31251ebbe8'}
    )
    json_response = r.json()
    print(json_response)
    output = json_response['output']
    neutral_count = 0
    positive_count = 0
    negative_count = 0
    for o in output:
        if o == "Neutral":
            neutral_count += 1
        elif o == "Positive":
            positive_count += 1
        else:
            negative_count += 1
    if positive_count >= negative_count and positive_count >= neutral_count:
        score = 0.8
        sentiment = 'positive'
        magnitude = 1.3

    elif negative_count >= positive_count and negative_count >= neutral_count:
        score = -0.8
        sentiment = 'negative'
        magnitude = 1.3
    return sentiment, score, magnitude


if __name__ == '__main__':
    analyse_sentiment_deep_ai("hello world")