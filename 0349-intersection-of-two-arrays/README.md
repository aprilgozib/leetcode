<h2><a href="https://leetcode.com/problems/intersection-of-two-arrays">349. Intersection of Two Arrays</a></h2><h3>Easy</h3><hr><p>Given two integer arrays <code>nums1</code> and <code>nums2</code>, return <em>an array of their <span data-keyword="array-intersection">intersection</span></em>. Each element in the result must be <strong>unique</strong> and you may return the result in <strong>any order</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [1,2,2,1], nums2 = [2,2]
<strong>Output:</strong> [2]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [4,9,5], nums2 = [9,4,9,8,4]
<strong>Output:</strong> [9,4]
<strong>Explanation:</strong> [4,9] is also accepted.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums1.length, nums2.length &lt;= 1000</code></li>
	<li><code>0 &lt;= nums1[i], nums2[i] &lt;= 1000</code></li>
</ul>

## Approach
use sort, two pointers, consider duplicate
- nums1.sort()
- nums2.sort()
- i, j = 0,0
- res = []
- while i < len(nums1) & j < len(nums2):
	- if nums1[i] == nums2[j]:
 		- res.append(nums1[i])
   		- i += 1
     	- j += 1
      	- while i < len(nums1) & nums1[i] == nums1[i-1]: # manage duplicate
      		- i += 1
      	- while j < len(nums2) & nums2[j] == nums2[j-1]:
      		- j += 1
    - elif nums1[i] < nums2[j]:
    	- i += 1
    - else:
    	- j += 1
- return res

time complexity : O(nlogn), space complexity : O(1)  
thinking about handling duplicate like [2,2]

## Approach
use set
- return list(set(nums1) & set(nums2))

time complexity : O(n), space complexity : O(n)  
using set -> no need sort, using & to find intersection 
