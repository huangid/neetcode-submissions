class Solution:
    def simplifyPath(self, path: str) -> str:
        sPath = []
        split = path.split("/")
        for word in split:
            if word == "..":
                if sPath:
                    sPath.pop()
            elif word != "" and word != ".":
                sPath.append(word)
        return "/" + "/".join(sPath)