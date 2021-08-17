class Solution:
    def can_be_formed(self, word, chars):
        for char in word:
            if char in chars:
              chars = chars.replace(char, '', 1)
            else:
                return False
        return True
    
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = 0
        for word in words:
            if self.can_be_formed(word, chars):
                count += len(word)
        return count
    
        