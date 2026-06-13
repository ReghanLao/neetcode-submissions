class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        min_speed = max(piles)

        while left <= right:
            mid = (left + right) // 2
            hours = 0

            for pile in piles:
                hours += math.ceil(pile / mid)
            
            if hours <= h:
                min_speed = min(min_speed, mid)
                right = mid - 1
            elif hours > h:
                left = mid + 1
            
        return min_speed
