class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word_end = False


class Trie:
    def __init__(self):
        self.root_node = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root_node # let current node = root node
        for c in word:
            # find the child node of the current node associated with that letter
            # if there is no child node associated with that letter,
            # create a new node and add it to current node as a child associated 
            # with the letter
            if c not in node.children:
                node.children[c] = TrieNode(c)
                # set current node = child node
                node = node.children[c]
        node.is_word_end = True

    def search(self, word: str) -> bool:
        node = self.root_node
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.is_word_end

    def startsWith(self, prefix: str) -> bool:
        node = self.root_node
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        return True
