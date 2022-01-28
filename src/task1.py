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
                continue
            counter = 0
            for n in range(len(word)):
                if word[n] == "." or word[n] == m[n]:
                    counter += 1
                else:
                    break
                if counter == len(word):
                    return True

        return False



# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()

obj.addWord("a")
obj.addWord("aab")


param_2 = obj.search(".a.")
print(param_2)