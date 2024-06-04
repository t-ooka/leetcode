# 方法論

## Non ascii value

インプットされる値はASCIIのみなので、delimeterとしてnon-ascii値を採用する方法。（ex: π, あ)

時間計算量: o(n)
空間計算量: o(k)

## Escaping

エスケーピングを使用して、delimeterが元の文字列か判別がつくようにする手法。

- https://en.wikipedia.org/wiki/Escape_sequence

時間計算量: o(n)
空間計算量: o(k)

エスケープ関連
- [double-terminated-string](https://devblogs.microsoft.com/oldnewthing/20091008-00/?p=16443)
- [Protocol Buffers](https://ja.wikipedia.org/wiki/Protocol_Buffers)

## Chunked transfer encoding

もとの文字列の長さとdelimeterを使用して、chunk毎にもとの文字列長さがわかるようencodeする方法。

- https://en.wikipedia.org/wiki/Chunked_transfer_encoding

時間計算量: o(n)
空間計算量: o(k)


#　振り返り

## Step1

値がnon-asciiであるため、non-ascii値を使用してjoin,splitを使用としたが、スペースもascii値であることに気づいておらず失敗。

```step1.py
class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        return ' '.join(strs)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        if s == '':
            return [""]
        else:
            return s.split()


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
```

