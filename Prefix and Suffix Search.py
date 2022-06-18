# 745. Prefix and Suffix Search

# Design a special dictionary with some words that searchs the words in it by a prefix and a suffix.

# Implement the WordFilter class:

# WordFilter(string[] words) Initializes the object with the words in the dictionary.
# f(string prefix, string suffix) Returns the index of the word in the dictionary, which has the prefix prefix and the suffix suffix. If there is more than one valid index, return the largest of them. If there is no such word in the dictionary, return -1.

class WordFilter:

    def __init__(self, words: List[str]):
        self.d = {}
        for i, word in enumerate(words):
            for p, s in product(range(len(word) + 1), repeat=2):
                self.d[word[:p], word[s:]] = i

    def f(self, prefix: str, suffix: str) -> int:
        return self.d.get((prefix, suffix), -1)


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)