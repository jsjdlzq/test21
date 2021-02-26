def even(a):                                  #函数定义
    if a%2 == 0:
        print("该数为偶数")
    else:
        print("该数为奇数")                    #如果能被2整除输出偶数，如果不能整除则是奇数


b = (input("请输入一个整数:"))                  #对b进行赋值
while not b.isdigit():                       #使用while语句，对输入的值进行是否是数字的判断，如果不是数字进行重新输入
    b = input("输入类型有误，请重新输入一个整数：")
else:
    even(int(b))                              #调用函数
