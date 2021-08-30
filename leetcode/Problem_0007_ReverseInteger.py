class Solution:
    def reverse(self, x: int) -> int:
        if x < -2**31 or x > 2**31 -1:
            return 0

        neg = True if (x >> 31 & 1) == 1 else False  # 判断是否为负数

        x = x if neg else -x  # 转换为负数，负数最小值范围比正数最大值范围大
        min_val = -2**31  # 系统最小值

        # python3 使用正数做除法
        # 5 // 2 = 2  ,  -5 // 2 = -3
        div = -(abs(min_val) // 10)
        mod = -(abs(min_val) % 10)
        res = 0
        while (x != 0):
            if -res < div or (-res == div and abs(x%10) < mod):
                # 溢出
                return 0
            res = res * 10 + abs(x) % 10
            x = abs(x) // 10
            x = x if neg else -x

        res = -res if neg else res
        return res


if __name__ == '__main__':
    so_obj = Solution()
    res = so_obj.reverse(1563847412)

    print(res)


