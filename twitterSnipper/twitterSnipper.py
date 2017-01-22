# TwitterSnipper 
# filters duplicate tweets from a twitter list (provided by sys.argv[1]), from maxNumberOfTweets (provided by sys.arg[2])

import tweepy, shelve, datetime, sys
from keys import TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET

def init():
    global api
    auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
    auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET)
    api = tweepy.API(auth)
    

def filter(text, shelfFile, todaysTweetsList, weekdays):
    foundDuplicate = False
    
    for tweet in todaysTweetsList:
        if text[0:40].lower() in tweet:
            foundDuplicate = True
            break
    
    for day in weekdays:
        for i in shelfFile[day]:
            if text[0:40].lower() in i:
                foundDuplicate = True
                break
                  
    return foundDuplicate
    
    
def main():
            
    init()
    tweetCount = 0
    WEEKDAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    
    username = api.me().screen_name
    mySlug = sys.argv[1]                           # or change to name of your list
    maxNumberOfTweets = int(sys.argv[2])           # or change to number as needed, or set to None
    now = datetime.datetime.now()
    currentDate = now.strftime('%Y-%m-%d')
    weekday = now.strftime('%A')
    fileObj = open(username + "_" + mySlug + ".txt", "w") 
    
    shelfFile = shelve.open('twitterSnipper_' + mySlug)
    
    if len(list(shelfFile.keys())) != 0:
        lastSavedTweet = shelfFile['lastSavedTweet']
        lastDate = shelfFile['date']
        if currentDate != lastDate:
            todaysTweetsList = []
        else:
            todaysTweetsList = shelfFile[weekday]
    else:
        lastSavedTweet = None
        todaysTweetsList = []
        for day in WEEKDAYS:
            shelfFile[day] = ''
        
  
    for tweet in tweepy.Cursor(api.list_timeline, username, mySlug, since_id = lastSavedTweet).items(maxNumberOfTweets):       
        
        foundDuplicate = filter(tweet.text, shelfFile, todaysTweetsList, WEEKDAYS)
        
        if foundDuplicate == False:
            fileObj.write(tweet.author._json['screen_name'] + ":\t" + tweet.text + "\n\n\n")
            todaysTweetsList.append(tweet.text.lower())
            tweetCount += 1
        
        if tweetCount == 1:
            lastSavedTweet = tweet.id
                
    shelfFile[weekday] = todaysTweetsList
    shelfFile['lastSavedTweet'] = lastSavedTweet
    shelfFile['date'] = currentDate
    shelfFile.close()    
    

    fileObj.write("YOUR TWITTER {}\n{}\nTweets displayed: {}\n" .format(mySlug.upper(), now.strftime('%Y/%m/%d   %H:%M'), tweetCount))
    fileObj.close()
    
    
    
if __name__ == "__main__":
    main()
