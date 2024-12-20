"""Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the 10 most recent tweets in the user's news feed.

Implement the Twitter class:

Twitter() Initializes your twitter object.
void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId. Each call to this function will be made with a unique tweetId.
List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user themself. Tweets must be ordered from most recent to least recent.
void follow(int followerId, int followeeId) The user with ID followerId started following the user with ID followeeId.
void unfollow(int followerId, int followeeId) The user with ID followerId started unfollowing the user with ID followeeId."""

from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list) # userId -> list of [count, tweetIds]
        self.followMap = defaultdict(set) # userId -> set of followeeId
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        # Append tweet with a count to the user's tweet list
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1
  
    def getNewsFeed(self, userId: int) -> List[int]:
        res = [] # Ordered list starting from recent tweets
        minHeap = []

        # User follows themselves by default
        self.followMap[userId].add(userId)
        
        # Gather all tweets from the user's followees into a min-heap
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                # Get the latest tweet from each followee
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]
                minHeap.append([count, tweetId, followeeId, index - 1])
        
        # Turn the list into a heap
        heapq.heapify(minHeap)
        
        # Extract up to 10 most recent tweets
        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)

            # If there are more tweets left for this followee, add the next one to the heap
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        # Add the followee to the follower's following list
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # Remove the followee from the follower's following list
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
