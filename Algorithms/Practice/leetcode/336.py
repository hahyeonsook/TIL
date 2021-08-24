import collections
from typing import List


class TrieNode:
    def __init__(self) -> None:
        self.children = collections.defaultdict(TrieNode)
        self.word_id = -1
        self.palindrome_word_ids = []


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    @staticmethod
    def is_palindrome(word: str) -> bool:
        return word[::] == word[::-1]

    # 단어 삽입
    def insert(self, index: int, word: str) -> None:
        node = self.root
        # 단어를 뒤집어서 입력
        for i, char in enumerate(reversed(word)):
            if self.is_palindrome(word[0 : len(word) - i]):
                node.palindrome_word_ids.append(index)
            node = node.children[char]
        node.word = index

    # 단어 존재 여부 판별
    def search(self, index: int, word: str) -> List[List[int]]:
        results = []
        node = self.root

        while word:
            # 판별 로직 3
            # 탐색 중간에 word_id가 있고, 나머지 문자가 펠린드롬인 경우
            # dcbc + d
            # d 의 word_id가 -1이 아니고 남은 문자가 펠린드롬인 경우, 두 단어의 합은 펠린드롬.
            if node.word_id >= 0:
                if self.is_palindrome(word):
                    results.append([index, node.word_id])
            if not word[0] in node.children:
                return results
            node = node.children[word[0]]
            word = word[1:]

        # 판별 로직 1
        # 끝까지 탐색했을 때, word_id가 있는 경우
        # 들어온 word와 거꾸로 입력한 word는 인덱스가 다른데, 순서가 같으므로 두 개의 합은 펠린드롬임.
        if node.word_id >= 0 and node.word_id != index:
            results.append([index, node.word_id])

        # 판별 로직 2
        # 끝까지 탐색했을 때, palindreom_word_ids가 있는 경우
        # dcbb + [남은 단어] + bbcd
        # 끝까지 탐색하고 단어가 같을 때, 남은 단어들이 펠린드롬이면, 두 단어의 합은 펠린드롬임.
        for palindrome_word_id in node.palindrome_word_ids:
            results.append([index, palindrome_word_id])

        return results


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        trie = Trie()

        for i, word in enumerate(words):
            trie.insert(i, word)

        results = []
        for i, word in enumerate(words):
            results.extend(trie.search(i, word))

        return results


words = ["d", "cbbcd", "dcbb", "dcbc", "cbbc", "bbcd"]
sol = Solution()
print(sol.palindromePairs(words))
