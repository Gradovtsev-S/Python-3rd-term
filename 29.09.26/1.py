from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count_magazine = Counter(magazine)
        count_ransom = Counter(ransomNote)

        for char, count in count_ransom.items():
            if count_magazine[char] < count:
                return False
        return True