import sys, collections

input = sys.stdin.readline


class TrieNode:
    def __init__(self) -> None:
        self.word = False
        self.children = collections.defaultdict(TrieNode)


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            node = node.children[char]
        node.word = True

    # prefix로 단어가 시작하는지 검사
    def startsWith(self, prefix):
        node = self.root
        for char in prefix:
            # char가 node의 children에 없으면 시작하지 않는 것으로 return
            if char not in node.children:
                return False
            node = node.children[char]
        if node.children:
            return True
        return False


def solution(T):
    for _ in range(T):
        N = int(input().strip())
        answer = "YES"

        book = Trie()
        numbers = []
        for _ in range(N):
            number = input().strip()

            book.insert(number)
            numbers.append(number)

        for number in numbers:
            # number로 시작하면 True, 시작하지 않으면 False
            if book.startsWith(number):
                answer = "NO"
        print(answer)


T = int(input().strip())
solution(T)
