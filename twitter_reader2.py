import snscrape.modules.twitter as sntwitter
import datetime



def tweet_reader(teams:dict):
    for handle in teams.values():
        # scraper = sntwitter.TwitterSearchScraper('from:' + handle)
        scraper = sntwitter.TwitterUserScraper(handle)
        tweets = scraper.get_items()
        tweet = next(tweets)
        if tweet.date.date() != datetime.date.today():
            continue
        print(str(tweet.user) + ' ' + str(tweet.date))
