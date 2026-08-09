class Solution:
    def compress(self, chars: List[str]) -> int:
        read = write = 0
        n = len(chars)
        while read < n:
            ch = chars[read]
            count = 0
            while read < n and chars[read] == ch:
                read += 1
                count += 1
            chars[write] = ch
            write += 1
            if count > 1:
                for num in str(count):
                    chars[write] = num
                    write += 1

        return write