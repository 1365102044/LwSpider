
class test7:
    def __init__(self):
        print('************from test7.py**********')



class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            str_tem = str(x)
            str1 =  str_tem[1,len(str_tem)-1]
            res = self.tem_reverse(str1)
            res1 = res[0]
            while(res1 == '0'):
                res.remove(res1)
                res1 = res[0]
            return int('-'+str(res))

    def tem_reverse(self, num):
        nums = list(str(num))
        start = 0
        end = num.length
        while (start <= end):
            tem = nums[start]
            nums[start] = nums[end]
            nums[end] = tem
        return nums





if __name__ == '__main__':
    res = Solution().reverse(-2340)
    print(res)
