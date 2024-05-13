## Step1

- k elementsのカウントをするところまではすぐ思いついた
- top k elementsをどのように最終的に配列の形で返すかわからず、以降のコードが進まなくなった


## Step2

確認した解法
1. ヒープを使用した方法(n log k)
2. 配列とハッシュマップを使用した方法

学んだこと
- Counterを使用して簡単に要素のカウントができること。
- Bucket Sortの応用として、インデックスに要素数、値に対応する配列をいれる方法。
- heapの基本アルゴリズム`Get Max or Min: O(n), Push: O(log n), Pop: (O log n)`
- [`heapq`モジュール](https://docs.python.org/ja/3/library/heapq.html#heapq.nlargest)
