class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        modified_string = ""
        min_length = min(len(word1), len(word2))

        for i in range(min_length):
            modified_string += word1[i] + word2[i]

        if len(word1) > len(word2):
            modified_string += word1[min_length:]
        elif len(word2) > len(word1):
            modified_string += word2[min_length:]

        return modified_string

solution = Solution()
print(solution.mergeAlternately(word1="abc", word2="pqr"))
print(solution.mergeAlternately(word1="ab", word2="pqrs"))
print(solution.mergeAlternately(word1="abcd", word2="pq"))