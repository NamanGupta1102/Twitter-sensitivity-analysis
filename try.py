import tweepy
bearer_token = "AAAAAAAAAAAAAAAAAAAAAPezcQEAAAAApl094xJm8bSnFr%2B6qKdAouHPYhw%3DwBCeYTEiK6ah58QXc9wAtK4lcshqShKZoQXr2ZLGk5RSzlqXu1"
consumer_key = "IeGiAiHpNNojEvu6EgFJk3rsX"
consumer_secret = "nYC0eJ7xCUh8F3KnP7ozREUQKYNs4s3j44H8bMIc16UIQBqJGs"
access_token = "971077863444176896-90bZdNm5XreaxvvUToDZQJtS6v6cLyx"
access_token_secret = "WX7tMSIEQGuBxF055lz8hjgMsc7PLROH80jf00gxLuvVw"
client = tweepy.Client(bearer_token=bearer_token)
client = tweepy.Client(
    consumer_key=consumer_key, consumer_secret=consumer_secret,
    access_token=access_token, access_token_secret=access_token_secret
)
print(dir(client))

tweet_ids = [1460323737035677698, 1293593516040269825, 1293595870563381249]
response = client.get_tweets(tweet_ids, tweet_fields=["created_at"])
for tweet in response.data:
    print(tweet.id, tweet.created_at)
