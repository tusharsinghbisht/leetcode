class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordListSet = set(wordList)
        wordListSet.add(beginWord)
        queue = deque([(beginWord, 1)])
        visited = set()
        while queue:
            word, length = queue.popleft()
            visited.add(word)

            if word == endWord:
                return length

            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    next_word = word[:i] + c + word[i+1:]
                    if next_word in wordListSet:
                        wordListSet.remove(next_word)
                        queue.append((next_word, length+1))
        
        return 0