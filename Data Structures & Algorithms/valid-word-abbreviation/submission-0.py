class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = 0
        j = 0
        while i < len(word) and j < len(abbr):
            n = 0
            if abbr[j].isdigit():
                if abbr[j] == "0":
                    return False
                while j < len(abbr) and abbr[j].isdigit():
                    n = n*10 + int(abbr[j])
                    j += 1
                i += n
            else:
                if word[i] != abbr[j]:
                    return False
                i += 1
                j += 1
        return i == len(word) and j == len(abbr)
            