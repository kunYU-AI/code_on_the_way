# class Solution:
#     def JosephCircle(self, n, m):
#         circle = [i for i in range(n)]
#         idx = 0

#         while (len(circle) > 1):
#             idx = (idx + m - 1) % len(circle)
#             print(circle.pop(idx))

#         return circle[0]


# if __name__ == '__main__':
#     sol = Solution()
#     n = 5
#     m = 3
#     print("最后剩下的人:", sol.JosephCircle(n, m))


# --------------------------------------------------------------------- #

# class Solution:
#     def sorted_two_list(self , Input1, Input2):
#         l1 = len(Input1)
#         l2 = len(Input2)
#         merged_list = []

#         i, j = 0, 0
#         while (i < l1) and (j < l2):
#             if Input1[i] <= Input2[j]:
#                 merged_list.append(Input1[i])
#                 i += 1
#             else:
#                 merged_list.append(Input2[j])
#                 j += 1
        
#         if (i < l1):
#             merged_list.extend(Input1[i:])
        
#         if (j < l2):
#             merged_list.extend(Input2[j:])

#         return merged_list
    

# if __name__ == '__main__':
#     sol = Solution()
    
#     # 测试用例1：两个非空有序列表
#     Input1 = [1, 3, 5]
#     Input2 = [2, 4, 6]
#     print("测试用例1:", sol.sorted_two_list(Input1, Input2))  # 预期输出: [1, 2, 3, 4, 5, 6]

#     # 测试用例2：其中一个列表为空
#     Input3 = []
#     Input4 = [1, 2, 3]
#     print("测试用例2:", sol.sorted_two_list(Input3, Input4))  # 预期输出: [1, 2, 3]

#     # 测试用例3：两个列表均包含重复元素
#     Input5 = [1, 2, 2, 3]
#     Input6 = [2, 3, 4, 4]
#     print("测试用例3:", sol.sorted_two_list(Input5, Input6))  # 预期输出: [1, 2, 2, 2, 3, 3, 4, 4]

#     # 测试用例4：两个列表长度不同
#     Input7 = [1, 5, 9]
#     Input8 = [2, 3, 6, 10, 11]
#     print("测试用例4:", sol.sorted_two_list(Input7, Input8))  # 预期输出: [1, 2, 3, 5, 6, 9, 10, 11]

# ------------------------------------------------------------------ #

# class Solution:
#     def maxArray(self, arr: list) -> int: 
#         n = len(arr)

#         def recursion(arr, left, right):
#             if left == right:
#                 return arr[left]

#             mid = (left + right) // 2
#             leftSum = recursion(arr, left, mid)
#             midSum = self.crossSum(arr, left, mid, right)
#             rightSum = recursion(arr, mid+1, right)

#             return max(leftSum, midSum, rightSum)
        
#         return recursion(arr, 0, n-1)


#     def crossSum(self, arr, left, mid, right):
#         max_left_sum = float('-inf')
#         max_right_sum = float('-inf')
#         left_sum, right_sum = 0, 0

#         for i in range(mid, left-1, -1):
#             left_sum += arr[i]
#             max_left_sum = max(left_sum, max_left_sum)

#         for j in range(mid+1, right+1):
#             right_sum += arr[j]
#             max_right_sum = max(right_sum, max_right_sum)
        
#         return max_left_sum + max_right_sum


# if __name__ == '__main__':
#     sol = Solution()

#     # 测试用例1：普通情况
#     arr1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
#     print("测试用例1:", sol.maxArray(arr1))  # 预期输出: 6 (子数组 [4, -1, 2, 1])

#     # 测试用例2：全负数
#     arr2 = [-5, -3, -2, -1, -4]
#     print("测试用例2:", sol.maxArray(arr2))  # 预期输出: -1 (子数组 [-1])

#     # 测试用例3：全正数
#     arr3 = [1, 2, 3, 4, 5]
#     print("测试用例3:", sol.maxArray(arr3))  # 预期输出: 15 (整个数组)

#     # 测试用例4：单个元素
#     arr4 = [10]
#     print("测试用例4:", sol.maxArray(arr4))  # 预期输出: 10

#     # 测试用例5：包含0
#     arr5 = [1, -1, 0, 2, -3, 4]
#     print("测试用例5:", sol.maxArray(arr5))  # 预期输出: 4 (子数组 [4] 或 [0, 2, -3, 4])


# ----------------------------------------------------- #
# 求素数
def prime():
    is_prime = [True] * 1000  # 更直观的命名
    is_prime[0] = is_prime[1] = False  # 0和1不是素数
    
    for i in range(2, int(1000**0.5) + 1):  # 只需检查到平方根
        if is_prime[i]:
            for j in range(i*i, 1000, i):  # 从i*i开始标记
                is_prime[j] = False
    
    for i in range(2, 1000):
        if is_prime[i]:
            print(i)

prime()