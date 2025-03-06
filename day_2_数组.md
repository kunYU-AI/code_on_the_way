# 二维数组遍历技巧
## 151. 反转字符串中的单词
给你一个字符串s，请你反转字符串中单词的顺序。
单词是由非空格字符组成的字符串。s中使用至少一个空格将字符串中的单词分隔开。
返回单词顺序颠倒且单词之间用单个空格连接的结果字符串。
注意：输入字符串s中可能会存在前导空格、尾随空格或者单词间的多个空格。返回的结果字符串中，单词间应当仅用单个空格分隔，且不包含任何额外的空格。

### 解法1：双指针（反转数组）
```python
class Solution:
    def reverseWords(self, s: str) -> str:
        '''
        先整体反转，再部分反转
        '''
        # 左右指针
        # 空格处理
        s_list = []

        ls, rs = 0, len(s)-1
        while s[ls] == ' ' or s[rs] == ' ':
            if s[ls] == ' ':
                ls += 1
            if s[rs] == " ":
                rs -= 1
        
        prev = 'shit'
        for i in range(ls, rs+1):
            if s[i] == ' ' and prev == ' ':
                continue
            s_list.append(s[i])
            prev = s[i]
                        
        n = len(s_list)
        l, r = 0, n-1
        self.partial_reverse(s_list, l, r)

        # 快慢指针
        slow, fast = 0, 0
        while slow < n:
            if fast == n and s_list[slow] != " ":
                self.partial_reverse(s_list, slow, fast-1)
                break

            if s_list[fast] == " " and s_list[slow] == " ":
                fast += 1
                slow += 1
            elif s_list[fast] == " " and s_list[slow] != " ":
                self.partial_reverse(s_list, slow, fast-1)
                slow = fast
            elif s_list[fast] != " ":
                fast += 1
        
        return ''.join(s_list)

    def partial_reverse(self, lst, left, right):
        while left < right:
            lst[left], lst[right] = lst[right], lst[left]
            left += 1
            right -= 1
```

### 解法2：双端队列
```python
class Solution:
    def reverseWords(self, s: str) -> str:
        '''
        先整体反转，再部分反转
        '''
        # 左右指针
        # 空格处理
        s_list = []

        ls, rs = 0, len(s)-1
        while s[ls] == ' ' or s[rs] == ' ':
            if s[ls] == ' ':
                ls += 1
            if s[rs] == " ":
                rs -= 1
        
        prev = 'shit'
        for i in range(ls, rs+1):
            if s[i] == ' ' and prev == ' ':
                continue
            s_list.append(s[i])
            prev = s[i]
                        
        n = len(s_list)
        l, r = 0, n-1
        print(s_list)
        # 队列
        d, word = collections.deque(), []
        while l < n:
            if s_list[l] == ' ' and word:
                d.appendleft(''.join(word))
                word = []
            if s_list[l] != ' ':
                word.append(s_list[l])
            l += 1
        d.appendleft(''.join(word))

        return ' '.join(d)         
```

### 题注：
1. 双指针就是先整体反转，再局部反转的思路。处理空格稍微麻烦点。

