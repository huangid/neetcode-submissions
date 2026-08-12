class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0
        read = 0

        while read < len(chars):
            ch = chars[read]
            count = 0
            while read < len(chars) and ch == chars[read]:
                read += 1
                count += 1
            chars[write] = ch
            write += 1
            
            if count > 1:
                for n in str(count):
                    chars[write] = n
                    write += 1

        return write
