class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) == 1:
            return True
        elif word.islower() or word.isupper():
            return True
        elif word[0].isupper():
            remaining_letters = word[1:]
            if remaining_letters.islower():
                return True
        return False
        