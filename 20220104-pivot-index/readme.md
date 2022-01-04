# Pivot index

Given an array of integers, calculate the _pivot index_ of this array.

The _pivot index_ is the index where the sum of all the numbers **strictly** to the left of the index is equal to the sum of all the numbers **strictly** to the index's right.

If the index is on the left edge of the array, then the left sum is `0` because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.

[leetcode]: https://leetcode.com/problems/find-pivot-index/
