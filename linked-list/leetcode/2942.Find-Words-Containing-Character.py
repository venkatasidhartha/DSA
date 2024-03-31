
# my solution 
class Solution:
    def findWordsContaining(self, words: list[str], x: str) -> list[int]:
        arr = []
        for index,word in enumerate(words):
            if x in word:
                arr.append(index)
        return arr


Solution().findWordsContaining(words = ["leet","code"], x = "e")