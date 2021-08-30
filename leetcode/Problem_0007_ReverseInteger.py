class Solution:
    def reverse(self, x: int) -> int:
        neg = True if (x >> 31 & 1) == 1 else False  # 判断是否为负数
        print(f"neg: {neg}")

        x = x if neg else -x  # 转换为负数，负数最小值范围比正数最大值范围大
        print(f"x: {x}")

        res = 0
        while (x != 0):
            print(f"loop  x: {x}")
            import pdb;pdb.set_trace()
            res = res * 10 + x % 10
            x = abs(x) // 10

        return res


if __name__ == '__main__':
    so_obj = Solution()
    res = so_obj.reverse(-123)
    print(res)


