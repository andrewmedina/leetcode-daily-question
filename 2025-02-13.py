import heapq
from typing import List

# Time Complexity: O(NLogN)
# Space Complexity: O(N)
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # Convert the list into a min-heap for efficient extraction of the smallest elements
        heapq.heapify(nums)
        num_ops = 0  # Counter for the number of operations performed
        # Continue combining the smallest two elements until the smallest element meets or exceeds k
        while nums[0] < k:
            # Extract the two smallest elements
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            # Apply the operation: (2 * smaller element) + larger element
            new_val = min(x, y) * 2 + max(x, y)
            # Push the new value back into the heap
            heapq.heappush(nums, new_val)
            num_ops += 1  # Increment the operation count
        return num_ops  # Return the total number of operations performed
