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

## Chunked transfer encoding

もとの文字列の長さとdelimeterを使用して、chunk毎にもとの文字列長さがわかるようencodeする方法。

- https://en.wikipedia.org/wiki/Chunked_transfer_encoding

時間計算量: o(n)
空間計算量: o(k)


#　振り返り

## Step1
