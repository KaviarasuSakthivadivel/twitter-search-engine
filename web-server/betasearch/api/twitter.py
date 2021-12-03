import tweepy

# Oauth keys
consumer_key = "JKbniPsCAwpK0LRWUG3fVRS7f"
consumer_secret = "SLaBoO0d5ed9kdnRbIoo37tvDdzhtIoNuLK9VYfuZnDoY6MJ28"
access_token = "1432412039570497538-FuTSiTBArthte6iBExbQ1WXFDDWsnC"
access_token_secret = "jhLkbdjYRgcVSCgeXnwDA1XZvn1KT83htsTQydgcqMXQk"


class Twitter:
    def __init__(self):
        self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        self.auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(self.auth, wait_on_rate_limit=True)
        self.TwitterClient = tweepy.Client(
            bearer_token="AAAAAAAAAAAAAAAAAAAAANyCTQEAAAAAzmZ8xj48ibF%2Bsqaoko%2Bn0423A28%3DbNZONhjDVgLtOL2NBXmjHjuqnjmJv7cSoGJi9bzepHvhAtUEXo",
            wait_on_rate_limit=True)

    def _meet_basic_tweet_requirements(self, ):
        raise NotImplementedError

    def get_tweets_by_poi_screen_name(self, screen_name, tweet_count):
        result = tweepy.Cursor(self.api.user_timeline, screen_name=screen_name, exclude_replies=True, include_rts=False,
                               tweet_mode='extended', timeout=999999).items(tweet_count)
        return result

    def get_reply_info(self, reply_id):
        reply_withInfo = self.api.get_status(reply_id, include_entities=True)
        return reply_withInfo

    # def get_tweet_text(self,id):
    # return self.api.get_status(id, tweet_mode = 'extended').full_text

    def get_tweets_by_lang_and_keyword(self, tweet_count, keyword_value, tweet_lang):
        # place_fieldsList=["country","geo","country_code"]
        # user_fieldsList=["id","name","username"]
        return tweepy.Cursor(self.api.search_tweets, q=keyword_value + " -filter:retweets", lang=tweet_lang,
                             count=tweet_count, tweet_mode='extended').items(tweet_count)

    def get_replies(self, tweet_id, reply_count):
        tweet_fieldsList = ["id", "in_reply_to_user_id", "created_at", "lang"]
        user_fieldslist = ["verified"]
        # place_fieldsList=["country","geo","country_code"]
        expansions_list = ["author_id", "entities.mentions.username"]

        all_replies = tweepy.Paginator(self.TwitterClient.search_recent_tweets, query="conversation_id:" + tweet_id,
                                       tweet_fields=tweet_fieldsList, expansions=expansions_list,
                                       user_fields=user_fieldslist).flatten(limit=reply_count)
        return all_replies

    def get_metrics(self, tweet_ids):
        tweet_fieldsList = ["id", "public_metrics"]
        user_fieldsList = ["verified", "profile_image_url", "name", "username"]
        all_metrics = self.TwitterClient.get_tweets(tweet_ids, tweet_fields=tweet_fieldsList, expansions="author_id",
                                                   user_fields=user_fieldsList)
        tweet_metrics = all_metrics.data
        includes= all_metrics.includes
        if  bool(includes):
            user_metrics=includes["users"]
        
        metrics={}
        if tweet_metrics is not None:
            print(len(tweet_metrics))
            print(len(user_metrics))
            for i in range(len(tweet_metrics)):
                tweet_id=str(tweet_metrics[i]["id"])
                metrics[tweet_id]={}
                metrics[tweet_id]["retweet_count"]=tweet_metrics[i]["public_metrics"]["retweet_count"] if tweet_metrics[i]["public_metrics"]["retweet_count"] is not None else 0
                metrics[tweet_id]["reply_count"]=tweet_metrics[i]["public_metrics"]["reply_count"] if tweet_metrics[i]["public_metrics"]["reply_count"] is not None else 0
                metrics[tweet_id]["like_count"]=tweet_metrics[i]["public_metrics"]["like_count"] if tweet_metrics[i]["public_metrics"]["like_count"] is not None else 0
                metrics[tweet_id]["quote_count"]=tweet_metrics[i]["public_metrics"]["quote_count"]if tweet_metrics[i]["public_metrics"]["quote_count"] is not None else 0
                user_id=(tweet_metrics[i]["author_id"])
                user_idx=-1
                for k, dic in enumerate(user_metrics):
                    if dic["id"]==user_id:
                        user_idx=k
                        break
                    
            
                if user_idx>=0:
                    metrics[tweet_id]["username"]=user_metrics[user_idx]["username"]
                    metrics[tweet_id]["profile_name"]=user_metrics[user_idx]["name"]
                    metrics[tweet_id]["profile_url"]=user_metrics[user_idx]["profile_image_url"]
                    metrics[tweet_id]["verified"]=user_metrics[user_idx]["verified"]
                else:
                    metrics[tweet_id]["username"]=""
                    metrics[tweet_id]["profile_name"]=""
                    metrics[tweet_id]["profile_url"]=""
                    metrics[tweet_id]["verified"]=False
            


            


        
        # if not bool(includes):
        #     includes = None
        return metrics


if __name__ == '__main__':
    t = Twitter()
    print(t.get_metrics("1437216869597921283,1466240523740401664,1437214611762151426,1437213484156997634,1437206898378350592"))
    