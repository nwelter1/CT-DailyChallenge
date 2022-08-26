class Twitter:
    def __init__(self):
        self.users = {}
        self.tweetOrder = 1
        
    def setupUser(self, userId):
        self.users[userId] = {"posts": [],"following": set([userId])}
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.users:
            self.setupUser(userId)
        self.users[userId]["posts"].append((self.tweetOrder, tweetId))
        self.tweetOrder += 1
    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.users:
            self.setupUser(userId)
        following = self.users[userId]['following']
        feed = []
        for user in following:
            for post in self.users[user]["posts"]:
                feed.append(post)
        sort_feed = sorted(feed)
        if not len(sort_feed):
            return None
        return [x[1] for x in reversed(sort_feed[-10:])]
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users:
            self.setupUser(followerId)
        if followeeId not in self.users:
            self.setupUser(followeeId)
        self.users[followerId]['following'].add(followeeId)
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users:
            self.setupUser(followerId)
        if followeeId not in self.users:
            self.setupUser(followeeId)
        following = self.users[followerId]['following']
        if followeeId in following:
            self.users[followerId]['following'].remove(followeeId)
# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)