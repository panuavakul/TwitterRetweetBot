#!/usr/bin/env python
from google.appengine.ext import db
from bot import *

class LastReTweeted(db.Model):
    lastReTweetedId = db.IntegerProperty(required=True)


#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#


import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Nothing to see here. Go away!! Nooooooooo')
        #e = LastReTweeted(lastReTweetedId=600556123146489856)
        #e.put()
        #lastReTweeted=LastReTweeted.get_by_id(5629499534213120)
        #self.response.write(lastReTweeted.lastReTweetedId)
        #self.response.write('|||||')
        #try updating
        #lastReTweeted=LastReTweeted.get_by_id(5629499534213120)
        #lastReTweeted.lastReTweetedId=lastReTweeted
        #lastReTweeted.put()
        #self.response.write(lastReTweeted.lastReTweetedId)

class ReTweet(webapp2.RequestHandler):
    def get(self):
        retweetBot = Bot()
        retweetBot.retweetMember()

class FollowBack(webapp2.RequestHandler):
    def get(self):
        followbackBot = Bot()
        followbackBot.followBack()
class ReTweetAmatou(webapp2.RequestHandler):
    def get(self):
        retweetAmatou = Bot()
        retweetAmatou.retweetKeyword()

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/retweet', ReTweet),
    ('/followback', FollowBack),
    ('/retweetamatou', ReTweetAmatou)
], debug=True)

