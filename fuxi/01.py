# 变量的生命周期


# g = '我是全局变量' # 全局变量
# print('第一次打印全局变量', g)
# def var():
#     global g # 声明变量g为全局变量
#     g = '修改了全局变量g' # 修改全局变量g的值
#
# var()
# print('第二次打印全局变量', g)

# g = "全局变量01"
# print(g)
#
# def var():
#     global g
#     g = "全局变量02"
#
# var()
# print(g)


# g = '我是全局变量' # 全局变量
# print('第一次打印全局变量', g)
# def var():
#     g = '创建一个新的局部变量g' # 不使用global关键字，相当于重新创建了一个新的局部变量g
#
# var()
# print('第二次打印全局变量', g)


# g = '我是全局变量' # 全局变量
# print('第一次打印全局变量', g)
# print(id(g))
# def var():
#     f = g
#     f = '修改了全局变量g' # 虽然f引用了g的内存空间，但是无法修改全局变量g中的值，因为对f重新赋值，相当于f引用了其他内存空间，而g的引用没有被改变
#     print(id(f))
#
# var()
# print('第二次打印全局变量', g)









# # 变量的赋值魔法
# a = 1,2,3
# x,y,z = a # 元组解包赋值
# print(x)
# print(y)
# print(z)
#
# a = [1,2,3]
# x,y,z = a # 列表解包赋值
# print(x)
# print(y)
# print(z)
#
# a = {'name':'小明','age':18}
# x,y = a # 字典解包赋值，获取的是key的值
#
# print(x)
# print(y)
#
# a = {'小明',18}
# x,y = a # 集合解包赋值
# print(x)
# print(y)
#
#
# a = '小明'
# x,y = a # 字符串解包赋值
# print(x)
# print(y)

# # 切片
# a = "小明,小红,张"
# print(a.split(","))
#
# # 替换
# a = "小明,小红.张"
# a = a.replace(".",",")
# print(a)


# str="网站名称：{:>9s}\t网址：{:s}"
# print(str.format("果芽测开学院","www.stu.guoyasoft.com"))


# #以货币形式显示
# print("货币形式：{:,d}".format(1000000))
# #科学计数法表示
# print("科学计数法：{:E}".format(1200.12))
# #以十六进制表示
# print("100的十六进制：{:#x}".format(100))
# #输出百分比形式
# print("0.01的百分比表示：{:.0%}".format(0.01))



# # 元组常见操作
#
# l = ["小明","小张"]
# l.append("小红")
# print(l)
#
#
# l = ["小明","小张"]
# l.insert(1,"小红")
# print(l)

# l = [2,3,10,5,6,7,83,2,1,6,8]
# # 升序
# l.sort()
# print(l)
# # 降序
# l.sort(reverse=True)
# print(l)

d = {"name":"小明"}
d.update(sex="男",age=18)
print(d)

d = {"name":"小明"}
t = {"sex":"男","age":18}
d.update(t)
print(d)