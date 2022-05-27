from typing import List
from collections import deque


def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    wordList = set(wordList)
    queue = deque()
    queue.append(beginWord)
    if beginWord in wordList:
        wordList.remove(beginWord)
    level = 1
    while queue:
        size = len(queue)
        for s in range(0, size):
            currentWord = queue.popleft()
            if currentWord == endWord:
                return level
            for i in range(len(currentWord)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = currentWord[:i] + c + currentWord[i + 1:]
                    if next_word in wordList:
                        wordList.remove(next_word)
                        queue.append(next_word)
        level += 1
    return 0

