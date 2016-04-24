# coding: utf-8
from google.appengine.ext import db
import tweepy


class LastReTweeted(db.Model):
    lastReTweetedId = db.IntegerProperty(required=True)

class Bot():
    #declare class static variables for all the key stuff
    KEY = str()
    SECRET = str()
    TOKEN = str()
    TOKEN_SECRET = str()
    def __init__(self):
        #Read the dat file for key
        key = open("key.dat", "r+")
        self.KEY = key.readline()
        self.SECRET = key.readline()
        self.TOKEN = key.readline()
        self.TOKEN_SECRET = key.readline()

        key.close()
    #Tweet about random stuff on syrup
    def randomTweet(self):
        o = 0
    #retweet keyword that is not just sendai syrup
    def retweetKeyword2(self):
        #create the tweepy api for interface with tweeter
        consumer_key = self.KEY
        consumer_secret = self.SECRET

        access_token = self.TOKEN
        access_token_secret = self.TOKEN_SECRET

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        api = tweepy.API(auth)

        #creating ignore list, make thi global later
        ignoreList = ['syruprobot','sendai_syrup','ss_rukaaizawa','ss_annasato','ss_reinakikuchi','ss_kanasato','ss_sakiishikawa']
        #creating list of keyword
        keyword = [u"シロップ",u"れいな",u"さあきゅん",u"あんな",u"かな",u"るか",u"ルカ",u"玲菜",u"紗希",u"佳奈",u"瑠香",u"杏奈"]
        musictitle = [u"シェイクスピア",u"タラレバリロード",u"いつかはシャバダバ",u"愛と呼ぶらしい",u"女神ファンファーレ","Place with you","Special Day",u"桜色シンデレラ",u"せつなさを抱いて飛べ",u"君の背中"]
        withoutKeyword = [u"センダイシロップ"]


    def retweetKeyword(self):
        #create the tweepy api for interface with tweeter
        consumer_key = self.KEY
        consumer_secret = self.SECRET

        access_token = self.TOKEN
        access_token_secret = self.TOKEN_SECRET

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        api = tweepy.API(auth)

        #get the last retweet id and then retweet anything from the search
        lastReTweeted = LastReTweeted.get_by_id(5649391675244544)
        lastReTweetedId = lastReTweeted.lastReTweetedId
        originalLastReTweetedId = lastReTweetedId

        #create ignore list to save API call
        ignoreList = ['syruprobot','sendai_syrup','ss_rukaaizawa','ss_annasato','ss_reinakikuchi','ss_kanasato','ss_sakiishikawa']

        query = u"センダイシロップ"
        #do search and retweet
        for status in tweepy.Cursor(api.search,q=query.encode('utf-8'),since_id=str(lastReTweetedId)).items():
            if lastReTweetedId < status.id:
                lastReTweetedId = status.id
            #check if the screen_name is in our ignore list
            if not(status.user.screen_name in ignoreList):
                #check if it is a retweet
                 if not(hasattr(status, 'retweeted_status')):
                    #check if it is a reply
                    if status.in_reply_to_screen_name == None:
                        #find out if it had been retweeted have to do this because of stupid Twitter API bug
                        filteredStatus = api.get_status(status.id)
                        if filteredStatus.retweeted == False:
                            api.retweet(filteredStatus.id)

        #put the lastReTweetedId back
        if not(originalLastReTweetedId == lastReTweetedId):
            lastReTweeted.lastReTweetedId = lastReTweetedId
        lastReTweeted.put()



    #This method check if any follower are not being follow and follow them
    def followBack(self):
        #create the tweepy api for interface with tweeter
        consumer_key = self.KEY
        consumer_secret = self.SECRET

        access_token = self.TOKEN
        access_token_secret = self.TOKEN_SECRET

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        api = tweepy.API(auth)

        for follower in tweepy.Cursor(api.followers).items():
            follower.follow()

    def retweetMember(self):
        #create the tweepy api for interface with tweeter
        consumer_key = self.KEY
        consumer_secret = self.SECRET

        access_token = self.TOKEN
        access_token_secret = self.TOKEN_SECRET

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        api = tweepy.API(auth)

        #find out the last retweet ID from the database
        #5629499534213120 is the id for the entry
        #get the entity by using get by id
        lastReTweeted = LastReTweeted.get_by_id(5629499534213120)
        lastReTweetedId = lastReTweeted.lastReTweetedId
        originalLastReTweetedId = lastReTweetedId

        #retweet everything while updating the lastReTweetedId to the maximum one
        for status in tweepy.Cursor(api.list_timeline,'syruprobot','member',since_id=str(lastReTweetedId)).items():
            # process status here
            #print status.text
            #check if it is already retweeted
            if status.retweeted == False:
                if lastReTweetedId < status.id:
                    lastReTweetedId = status.id
                api.retweet(status.id)
        #put the lastReTweetedId back
        if not(originalLastReTweetedId == lastReTweetedId):
            lastReTweeted.lastReTweetedId = lastReTweetedId
        lastReTweeted.put()




    #def __init__(self):
    #def saveImage(self):
    #def tweetImage(self):