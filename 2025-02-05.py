# Time Complexity: O(N)
# Space Complexity: O(1)
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        # Variables to track the indices of differing characters and the number of differences
        first_index_diff = second_index_diff = num_diffs = 0
        # Iterate through the strings to find differing positions
        for letter_ind in range(len(s1)):
            if s1[letter_ind] != s2[letter_ind]:  # Found a mismatch
                if (
                    num_diffs == 2
                ):  # More than two mismatches mean we can't swap to fix it
                    return False
                elif num_diffs == 1:  # If this is the second mismatch, store its index
                    second_index_diff = letter_ind
                else:  # If this is the first mismatch, store its index
                    first_index_diff = letter_ind
                num_diffs += 1  # Increment the number of mismatches found
        # Check if swapping the mismatched characters would make the strings equal
        return (
            s1[first_index_diff]
            == s2[second_index_diff]  # First mismatch should match second mismatch
            and s1[second_index_diff]
            == s2[first_index_diff]  # Second mismatch should match first mismatch
        )
