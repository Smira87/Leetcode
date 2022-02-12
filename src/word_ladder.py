from collections import defaultdict
from collections import deque

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0

        wordHash = self.buildHash(wordList)

        return self.bfs(beginWord, endWord, wordHash)

    def buildHash(self, wordList):
        wordHash = defaultdict(list)
        for word in wordList:
            # Put * in every possible index and add up its prefix and suffix
            for i in range(len(wordList[0])):
                prefix = word[:i]
                suffix = word[i + 1:]
                wordHash[prefix + '*' + suffix].append(word)
        return wordHash

    def bfs(self, beginWord, endWord, wordHash):
        visited = {}
        queue = deque([[beginWord, 1]])
        while queue:
            popWord, level = queue.pop()
            visited[popWord] = True

            for i in range(len(popWord)):
                prefix = popWord[:i]
                suffix = popWord[i + 1:]
                key = prefix + '*' + suffix

                for nextWord in wordHash[key]:

                    if nextWord == endWord:
                        return level + 1
                    if nextWord not in visited:
                        queue.append([nextWord, level + 1])
                wordHash[key] = []

        return 0




sol = Solution()

beginWord = "hot"
endWord = "dog"
wordList = ["hot","cog","dog","tot","hog","hop","pot","dot"]

#print(sol.ladderLength(beginWord, endWord, wordList))

hashWord = sol.buildHash(wordList)

print(sol.ladderLength(beginWord, endWord, wordList))