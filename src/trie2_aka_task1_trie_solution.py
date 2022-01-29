class TrieNode:

    def __init__(self, char) :

        self.char = char

        self.is_end = False

        self.children = {}

class Trie(object) :

    def __init__(self):

        self.root = TrieNode("")

    def insert(self, word):

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
                    if self.dfs(word[i+1:], child):
                        return True
            else:
                return False

        if node.is_end:
            return True
        else:
            return False


    def search(self, word):
        return self.dfs(word, self.root)



tr = Trie()
tr.insert("here")
tr.insert("hear")
tr.insert("he")
tr.insert("hello")
tr.insert("how ")
tr.insert("her")

print(tr.search("h."))


