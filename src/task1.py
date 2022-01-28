class WordDictionary(object):

    def __init__(self):
        self.set = set()

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        self.set.add(word)

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word in self.set:
                return True

        for m in self.set:
            if len(word) != len(m):
                break
            counter = 0
            for n in range(len(word)):
                if word[n] == m[n] or word[n] == '.':
                    counter += 1
                if counter == len(word):
                    return True

        return False



# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()

obj.addWord("word")
obj.addWord("lala")
obj.addWord("word")


param_2 = obj.search("w..d")
print(param_2)