<h2><a href="https://leetcode.com/problems/third-maximum-number">414. Third Maximum Number</a></h2><h3>Easy</h3><hr><p>Given an integer array <code>nums</code>, return <em>the <strong>third distinct maximum</strong> number in this array. If the third maximum does not exist, return the <strong>maximum</strong> number</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,2,1]
<strong>Output:</strong> 1
<strong>Explanation:</strong>
The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2]
<strong>Output:</strong> 2
<strong>Explanation:</strong>
The first distinct maximum is 2.
The second distinct maximum is 1.
The third distinct maximum does not exist, so the maximum (2) is returned instead.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,2,3,1]
<strong>Output:</strong> 1
<strong>Explanation:</strong>
The first distinct maximum is 3.
The second distinct maximum is 2 (both 2&#39;s are counted together since they have the same value).
The third distinct maximum is 1.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-2<sup>31</sup> &lt;= nums[i] &lt;= 2<sup>31</sup> - 1</code></li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> Can you find an <code>O(n)</code> solution?

## Approach
use float('-inf')
- f_max, s_max, t_max = float('-inf'), float('-inf'), float('-inf')
- for i in nums:
	- if i == f_max or i == s_max or i == t_max: #skip duplicate
 		- continue
	- if i > f_max:
 		- t_max = s_max
   		- s_max = f_max
     	- f_max = i
   - elif i > s_max:
   		- t_max = s_max
     	- s_max = i
   - elif:
   		- t_max = i
 - if t_max != float('-inf'):
 	- return t_max
 - else:
 	- return f_max

time complexity : O(n), space complexity : O(1)  
remember float('inf') format, thinking about handle duplicate, return maximum is different 
