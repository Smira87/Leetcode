class WordDictionary(object):


    def __init__(self):

        self.root = TrieNode("")

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self.root

        for char in word:

            if char in node.children:
                node = node.children[char]
            else:
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node

        node.is_end = True
    def dfs(self, word, node):

        for i in range(0, len(word)):
            if word[i] in node.children:
                node = node.children[word[i]]
            elif word[i] == ".":
                for child in node.children.values():
                    if self.dfs(word[i + 1:], child):
                        return True
                return False
            else:
                return False


        if node.is_end:
            return True
        else:
            return False

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return self.dfs(word, self.root)

class TrieNode:

    def __init__(self, char) :

        self.char = char

        self.is_end = False

        self.children = {}


# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()

obj.addWord("mad")
#obj.addWord("aab")


param_2 = obj.search("m..")

print(param_2)