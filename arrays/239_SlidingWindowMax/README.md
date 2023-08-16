# Based on

[this leetcode solution](https://leetcode.com/problems/sliding-window-maximum/solutions/3915747/video-ex-amazon-explains-a-solution-with-python-javascript-java-and-c/)
and
[this video](http://www.youtube.com/channel/UC9RMNwYTL3SXCP6ShLWVFww?sub_confirmation=1)

## A main point of algorithm

This code implements the sliding window maximum algorithm. It maintains a deque q to track the maximum elements' indices within the sliding window of size k. As the window moves, it compares the current element with the back of the deque and updates the deque accordingly. It also adjusts the deque to retain only relevant indices within the window. When the window size reaches k, it appends the maximum element of the window to the result list res. This process continues until the entire input list is traversed, resulting in the list of maximum values for each window.

1. Initialize Variables:
   - Initialize an empty list res to store the result.
   - Initialize two pointers left and right to represent the sliding window.
   - Initialize an empty deque q to maintain indices of potentially maximum elements.

2. Sliding Window Loop:
   - While the right pointer is within the range of nums:
     - Compare nums[right] with the elements at the back of the deque q.
       - If q is not empty and nums[right] is greater than nums[q[-1]], remove the back element of q since it cannot be the maximum for the current window.
     - Append the current right index to the back of the deque q.

3. Adjust Left Pointer:
   - If the index at the f ront of q (maximum element index) is less than the left pointer, remove the front element of q since it's no longer relevant for the current window.

4. Calculate and Store Maximum Element:
   - If the current window size is equal to or larger than k:
     - Append the maximum element of the current window (the element at index q[0]) to the res list.

5. Adjust Left Pointer and Move Right Pointer:
   - Increment the left pointer by 1.

6. Move Right Pointer:
   - Increment the right pointer by 1.

7. Return Result:
   - Return the res list containing the maximum elements for each sliding window.
