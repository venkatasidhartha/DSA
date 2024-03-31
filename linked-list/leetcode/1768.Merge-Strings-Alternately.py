

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1 = [i for i in word1]
        word2 = [i for i in word2]
        specialCount = 1
        for i in range(len(word2)):
            word1.insert(specialCount,word2[i])
            specialCount+=2
        
        word1 = "".join(word1)
        return word1
    

print(Solution().mergeAlternately("abcd","pqrs12321"))
# print(Solution().mergeAlternately("ab","pqcd"))