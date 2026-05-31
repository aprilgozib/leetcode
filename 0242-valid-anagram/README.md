<h2><a href="https://leetcode.com/problems/valid-anagram">242. Valid Anagram</a></h2><h3>Easy</h3><hr><p>Given two strings <code>s</code> and <code>t</code>, return <code>true</code> if <code>t</code> is an <span data-keyword="anagram">anagram</span> of <code>s</code>, and <code>false</code> otherwise.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;anagram&quot;, t = &quot;nagaram&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">true</span></p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;rat&quot;, t = &quot;car&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">false</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length, t.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>s</code> and <code>t</code> consist of lowercase English letters.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> What if the inputs contain Unicode characters? How would you adapt your solution to such a case?</p>

## Approach
use dictionary
- seen = {}
- for ch in s:
	- seen[ch] = seen.get(ch, 0) + 1
- for ch in t:
	- if ch not in seen:
    	- return False
    - else:
    	- seen[ch] -= 1
- for value in seen.values():
	- if value < 0:
 		- return False
    - elif value > 0:
    	- return False
- return True

time complexity : O(n), space complexity : O(n)  
thinking about edge cases -> s can be longer, t can be longer
