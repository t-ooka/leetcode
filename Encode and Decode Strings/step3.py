class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded_string = ""

        for s in strs:
            encoded_string += str(len(s)) + "#" + s
        
        return encoded_string
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        decoded_strings = []
        i = 0

        while i < len(s):
            delim = s.find("#", i)
            word_length = int(s[i:delim])
            decoded_str = s[delim+1 : delim + 1 + word_length]
            decoded_strings.append(decoded_str)
            i = delim + 1 + word_length
        
        return decoded_strings
