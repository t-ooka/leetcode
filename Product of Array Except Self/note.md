# 方法論

## Left, Rightそれぞれからの積を配列として使用する方法

例
```sample.py
input = [1,2,3,4]

left = [1,2,6,24]
right = [24,12,4,1]
```

left,rightはそれぞれ、各々のインデックスの数までの積を表しているので、両隣の数の積を取れば自身をのぞいた積にになる。

- 時間計算量 o(n)
- 空間計算量 o(n)


## Left, Rightを配列として持たずに求める方法

Left,Rightの操作を返り値の配列に対して直接行う。

例
```sample.py
res = [0] * len(nums)
prefix = 1
for i in range(0, len(nums)):
  res[i] = prefix
  prefix *= nums[i]
        
suffix = 1
for i in range(len(nums)-1, -1, -1):
  res[i] *= suffix
  suffix *= nums[i]

return res
```

-時間計算量 o(n)
-空間計算量 o(1)


# 振り返り

## Step1
Left, Rightの方法で進めようとしたが、コーディングが遅く15分タイムアウト。

