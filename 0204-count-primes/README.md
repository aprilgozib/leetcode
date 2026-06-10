<h2><a href="https://leetcode.com/problems/count-primes">204. Count Primes</a></h2><h3>Medium</h3><hr><p>Given an integer <code>n</code>, return <em>the number of prime numbers that are strictly less than</em> <code>n</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 10
<strong>Output:</strong> 4
<strong>Explanation:</strong> There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 0
<strong>Output:</strong> 0
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = 1
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= n &lt;= 5 * 10<sup>6</sup></code></li>
</ul>

## Approach
use True False list to check prime
- if i < 2:
	- return 0
- is_prime = True * n # [T, T, T, T, T, ...]
- is_prime[0] = False
- is_prime[1] = False # [F, F, T, T, T, ...]
- for i in range(2, n):
	- if is_prime: # True
 		- for j in range(i*i, n, i): # i의 배수는 이전에 이미 처리 됨
   			- is_prime[j] = False 
- return sum(is_prime)

time complexity : O(nloglogn) -> n/2 + n/3 + n/5 ..., space complexity : O(n)  
using Ture False list, and sliding condition
