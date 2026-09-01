class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = 1 + counts.get(num, 0)
        items = list(counts.items())
        n = len(items)

        if k >= n:
            return [num for num, _ in items]
        
        target = n - k

        def partition(left: int, right: int, pivot_index: int) -> int:
            pivot_freq = items[pivot_index][1]

            items[pivot_index], items[right] = items[right], items[pivot_index]
            store_index = left

            for i in range(left, right):
                if items[i][1] < pivot_freq:
                    items[store_index], items[i] = items[i], items[store_index]
                    store_index += 1
            items[store_index], items[right] = items[right], items[store_index]
            return store_index
        
        def quickselect(left: int, right: int, k_smallest: int) -> None:
            if left == right:
                return
            pivot_index = random.randint(left, right)
            pivot_index = partition(left, right, pivot_index)

            if k_smallest == pivot_index:
                return
            elif k_smallest < pivot_index:
                quickselect(left, pivot_index - 1, k_smallest)
            else:
                quickselect(pivot_index + 1, right, k_smallest)
        
        quickselect(0, n - 1, target)
        top_k_nums = [num for num, _ in items[target:]]
        return top_k_nums
        
        
