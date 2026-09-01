class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = ""

        for s in strs:
            res += s.replace("/", "//") + "/:"
        return res

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res = []
        current_string = ""

        i = 0

        while i < len(s):
            if s[i:i+2] == "/:":
                res.append(current_string)
                current_string = ""
                i += 2
            elif s[i:i+2] == "//":
                current_string += "/"
                i += 2
            else:
                current_string += s[i]
                i += 1
        
        return res


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
