class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for num in nums:
            if num in counts:
                counts[num] += 1
            else: 
                counts[num] = 1
        
        top_k = dict(sorted(counts.items(), key=lambda item: item[1], reverse=True)[:k])

        return list(top_k.keys())