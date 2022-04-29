class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if not low % 2 and not high % 2: return (high - low) // 2
        elif low % 2 and not high % 2: return (high-low) // 2 + 1
        else: return (high-1 - (low+1)) // 2 + 2