import tweepy
import datetime

bearer_token = ''
client = tweepy.Client(bearer_token, wait_on_rate_limit=True)


class Count:
    def __init__(self, asset, start_time, end_time, keyword):
        self.asset = asset
        for i in range(len(asset)):
            self.asset[i] = self.asset[i] + ' ' + keyword
        self.start_time = datetime.datetime(start_time[0], start_time[1], start_time[2], start_time[3])
        self.end_time = datetime.datetime(end_time[0], end_time[1], end_time[2], end_time[3])

    def describe(self):
        print(self.asset)

    def count(self):
        total_counts = {}
        for query in self.asset:
            tw_count = client.get_recent_tweets_count(query=query, start_time=self.start_time,
                                                      end_time=self.end_time).data
            total_count = 0
            for i in tw_count:
                total_count += i['tweet_count']
            total_counts.update({query: total_count})
        return total_counts


cel = Count(['cel'], [2022, 8, 15, 0], [2022, 8, 21, 0], 'short squeeze')
print(cel.count())
