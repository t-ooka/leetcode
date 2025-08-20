# step1

単方向リストであり、昇順にソート済みである前提があったので、次のノードをチェックして数が重複していたらそのノードをスキップすればいいよなぁと考えた。

最初動かないコードが出来上がった。
```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
      node = head

      while node and node.next:
        if node.val == node.next.val:
          node.next = node.next.next
        node = node.next
      
      return head
```

これは、毎回のループで `node = node.next`をしてしまっていたことが原因で、途中の確認がスキップされてしまうケースがあったからでした。
同じ数が2つ以上続く場合は↑のコードだと上手くいかない。

## step2

解答を見て、考えていた内容と同じだったので再度コーディングを3回しました。

ループが回る回数は渡されるListNodeの連結数なので、時間計算量は O(N)。nodeを変数として扱いますが、空間計算量はListNodeの連結数には依存しないので O(1)と考えています。これは二重ループを使った場合も同様な認識です。ループ総数のオーダーは同じになる認識。

## step3

あまり変更点が思いつかず、そのままコーディングしました。
