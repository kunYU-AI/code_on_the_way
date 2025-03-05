## 83. 删除排序链表中的重复元素
给定一个已排序的链表的头head，删除所有重复的元素，使每个元素只出现一次。返回已排序的链表。

### 解法1：双指针（冗余写法）
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head

        while slow and slow.next:
            fast = fast.next

            if not fast:
                fast, slow = slow.next, slow.next
                continue

            if fast.val == slow.val:
                slow.next = fast.next
                fast.next = None
                fast = slow
            else: 
                slow = slow.next
        
        return head
```
### 题注：
1. 双指针是多余的写法。正确为单指针，检验当前node和下个node是否相等。
```python
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr = head
        while ptr.next:
            if ptr.val == ptr.next.val:
                ptr.next = ptr.next.next
            else:
                ptr = ptr.next
        return head 
```

## LCR 006. 两数之和 II - 输入有序数组 ⭐⭐
给定一个已按照升序排列的整数数组numbers，请你从数组中找出两个数满足相加之和等于目标数target。
函数应该以长度为2的整数数组的形式返回这两个数的下标值。numbers的下标从0开始计数，所以答案数组应当满足0 <= answer[0] < answer[1] < numbers.length。
假设数组中存在且只存在一对符合条件的数字，同时一个数字不能使用两次。

### 解法1：前后双指针
```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 前后双指针
        left, right = 0, len(numbers) - 1
        while left < right:
            sum_ = numbers[left] + numbers[right]
            if sum_ == target:
                return [left, right]
            elif sum_ < target:
                left += 1
            else:
                right -= 1
        return []

```


## 5. 最长回文子串 ⭐⭐⭐
给你一个字符串s，找到s中最长的回文子串。

### 解法1：中心扩散算法
```python 
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res = ''
        for i in range(n):
            s_odds = self.palindrome(s, i, i)
            s_even = self.palindrome(s, i, i+1)
            res = s_odds if len(s_odds) > len(res) else res
            res = s_even if len(s_even) > len(res) else res

        return res  

    def palindrome(self, s, i, j):
        # 以i为中心的最长回文子串
        while (i>=0) and (j<len(s)) and (s[i] == s[j]):
            i -= 1
            j += 1
        
        return s[i+1:j]
```

### 解法2: 动态规划
```python
# 状态：回文子串的长度（状态不作为dp数组的索引？）
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        max_len = 1
        begin = 0

        dp = [[False] * n  for _ in range(n)]
        for i in range(n):
            dp[i][i] = True

        # 迭代：
        # i必须小于j，且我们由中心向两边迭代
        for length in range(2, n+1):
            for i in range(n):
                j = i+length-1
                if j>=n:
                    break
                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    if j-i<3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]        
                
                if dp[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    begin = i

        return s[begin:begin + max_len] 
```

### 题注：
1. 状态并不一定作为DP数组的索引。重要是找到状态转移方程 = 找到重复发生的子问题。
2. 我们要达成的目标是：最长的回文子串，因此，在DP数组的迭代中，最终目标就是找不同选择下的最大状态（回文子串的长度）。
