import snscrape.modules.twitter as sntwitter
import re
import datetime



def tweet_reader(daily_dictionary: dict, reported_scores: list) -> None:


    tweet_container = []
    read_tweets = []

    score_regex = re.compile(r'''
            #[^:\n]
            \d{1,2}
            -
            \d{1,2}
            #[^:!.]
            ''', re.VERBOSE)

    for team_name, twitter_handle in daily_dictionary.items():
        #i've tried this next line as a way of just reading the top result. i need to test this while there are matches on
        # this may have sorted out the speed issue though.
        for tweet in sntwitter.TwitterSearchScraper('from:' + twitter_handle,
                                                                 mode=sntwitter.TwitterSearchScraperMode.TOP).get_items():
        #for i, tweet in enumerate(sntwitter.TwitterSearchScraper('from:'+twitter_handle, mode=sntwitter.TwitterSearchScraperMode.TOP).get_items()):
        ##for i, tweet in enumerate(sntwitter.TwitterSearchScraper('from:'+twitter_handle).get_items()):
            # if tweet.date.date() != datetime.date.today():
            #     break

            text = tweet.rawContent
            extract = score_regex.findall(text)
            if len(extract) > 0:
                extract_string = extract[0]
                extract_string = extract_string.replace('\n', '')
                extract_string = extract_string.replace(' ', '')
                if tweet.id not in read_tweets:
                    tweet_container.append([team_name, tweet.user.username, extract_string, tweet.id, tweet.date.date()])
                    read_tweets.append(tweet.id)

    for individual_tweet in tweet_container:
        reported_scores.append([individual_tweet[0], individual_tweet[2]])
        print(individual_tweet[0] + ' - ' + individual_tweet[1] + ' - ' + individual_tweet[2] + ' - ' + str(individual_tweet[4]))

