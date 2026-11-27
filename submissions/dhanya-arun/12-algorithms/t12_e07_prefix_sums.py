# T12-E07 Prefix sums
#
# Write these functions:
#
# - `build_prefix(nums)` returns a list where `prefix[i]` is the sum of `nums[0:i]`. The list has `len(nums) + 1` entries.
# - `range_sum(prefix, left, right)` returns the sum of `nums[left..right]`, inclusive, in O(1) time.
# - `equilibrium_index(nums)` returns the first index where the sum to its left equals the sum to its right, or `-1`.
# - `count_subarrays_with_sum(nums, k)` counts the subarrays that sum to `k`, in one pass, using a dict of prefix sums.
