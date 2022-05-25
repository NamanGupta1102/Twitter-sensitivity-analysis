tweet_ids = [1460323737035677698, 1293593516040269825, 1293595870563381249]
response = client.get_tweets(tweet_ids, tweet_fields=["created_at"])