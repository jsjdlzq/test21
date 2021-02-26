def max(a:int,b:int):                    #函数定义
    if a>b:
        return a
    else:
        return b                         #输入两个数，返回其中较大者
"""
初次使用github
测试使用
"""
a = int(input("请输入第一个数字："))
b = int(input("请输入第二个数字："))
c = max(a,b)
print("您输入的第一数是{a1},输入的第二个数是{b1},这两个数字中较大者是{c1}.".format(a1=a,b1=b,c1=c))