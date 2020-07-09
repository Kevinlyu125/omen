# def shang_yu(a,b):
#     if (b == 0):
#         print("除数不能为0")
#     else:
#         print(a // b, a % b)
#
# shang_yu(10,2)
# shang_yu(2,10)


# def shang_yu(a,b):
#     if (b == 0):
#         return None
#     else:
#         return(a // b, a % b)
# res = shang_yu(10,0)
# if res is None:
#      print("参数错误")
# else:
#      print(res[0],res[1])



# # global 全局函数
# a =12
# print(a)
#
# def aaa():
#     global a
#     a = 13
# aaa()
# print(a)

#
# # 类
# class clac():
#     a = None
#     b = None
#     res = None
#
#     def input(self,a,b):
#         self.a =a
#         self.b =b
#     def sum (self):
#         self.res = self.a + self.b
#     def div (self):
#         self.res = self.a / self.b
#     def get_result(self):
#         print(self.res)
#
# c = clac()
#
# c.input(10,20)
# c.sum()
# c.get_result()

# # 九九乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(j,"X",i,"=",i*j,end="\t")
#     print()

#冒泡函数

# a =[561,156,165,161,6,16,51,651,651,56,1]
# length = len(a)
# for i in range(length-1,0,-1):
#     for b in range(i):
#         if (a[b] > a[b+1]):
#             a[b],a[b+1] = a[b+1],a[b]
# print(a)





# l = [322,213,1213,1231]
#
# length = len(l)
# # print(length)
# for i in range (length-1,0,-1):
#     for j in range (i):
#         if (l[j] > l[j+1]):
#             l[j], l[j+1] = l[j+1], l[j]
# print(l)



# for i in range (1,10):
#     for j in range (1,i+1):
#         print(j, "x", i, "=", j * i, end="\t")
#
#     print()
#

ran = str(random.randint(1,10))
a = input("请输入1-9的数字")
if a != ran:
        print("很遗憾")
else:
    print("恭喜")