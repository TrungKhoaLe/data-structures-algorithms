from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current_node = self.root

        for c in word:
            if c not in current_node.children:
                new_node = TrieNode()
                current_node.children[c] = new_node
            current_node = current_node.children[c]
        current_node.is_word_end = True

    def search(self, word: str) -> str:
        current_node = self.root
        root = ""
        for c in word:
            if c not in current_node.children:
                break

            root += c
            current_node = current_node.children[c]
            if current_node.is_word_end:
                return root

        return word


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for root in dictionary:
            trie.insert(root)
        words = sentence.split()
        return " ".join([trie.search(word) for word in words])


if __name__ == '__main__':
    dictionary = ["cat", "rat", "bat"]
    sentence = "the cattle was rattled by the battery"
    solution_obj = Solution()
    print(solution_obj.replaceWords(dictionary, sentence))
