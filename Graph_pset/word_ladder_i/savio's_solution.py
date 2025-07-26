class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        dq = deque()
        dq.append((beginWord, 1))
        eliminate = set(wordList)

        if endWord not in eliminate:
            return 0
        while dq:
            start_word, step = dq.popleft()
            n = len(start_word)
            arr = [c for c in start_word]
            for i in range(n):
                curr_char = arr[i]
                nw_word = ""
                for j in range(ord('a'), ord('z') + 1):
                    arr[i] = chr(j)
                    nw_word = "".join(arr)
                    print(nw_word)
                    if nw_word in eliminate:
                        eliminate.remove(nw_word)
                        dq.append((nw_word, step + 1))
                    if nw_word == endWord:
                        return step + 1
                arr[i] = curr_char   
        return 0