import sys
import collections

input = sys.stdin.readline


class TrieNode:
    def __init__(self) -> None:
        self.key = None
        self.children = collections.defaultdict(TrieNode)


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, foods):
        node = self.root
        for floor, food in enumerate(foods):
            node = node.children[(floor, food)]
            node.key = (floor, food)

    def printTrie(self):
        node = self.root
        discovered = []
        stack = [node]

        while stack:
            v = stack.pop()
            if v not in discovered:
                if v != self.root:
                    print("--" * v.key[0], end="")
                    print(v.key[1])
                discovered.append(v)
                for w in sorted(v.children, reverse=True):
                    stack.append(v.children[w])


def solution(N):
    cave = Trie()
    for _ in range(N):
        cave.insert(input().split()[1:])

    cave.printTrie()


solution(int(input().strip()))
