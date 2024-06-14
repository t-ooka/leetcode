## Step1

#### 考えた解法
- ASCII値を使用して、1文字に対して一意なlistを作成し、それをキーとしてHashMapにいれる方法。

Time Complexity: N*K 
Space Complexity: N

(Nは要素数、Kは文字列の最大文字数)

#### メモ
- Hashmapの初期値をListにする方法が出てこなかったため、時間内にPassできず。


## Step2

#### 調べた解法
- Step1と同様にASCII値とListを使用した方法。
- ソートされた文字列をkeyとして使用する方法。(NKlogK for time comp, N for space comp)

#### メモ

- Hashmapの初期値をListにするには、[collections.defaultdict](https://docs.python.org/ja/3.6/library/collections.html#collections.defaultdict)が有効だった。
- 英小文字のASCII値は`ord('b') - ord('a')`のようにaのASCII値をシンプルに引けばよかったと気づき。

