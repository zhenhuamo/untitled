import random
import math
'''
输入一个三位数与程序随机数比较大小，
如果大于程序随机数，则输出这个三位数的个位、十位、百位
如果等于程序随机数，则提示中奖，记100分
如果小于程序随机数，则将120个字符输入到文本文件中
（规则是每一条字符串的长度为12，单独占一行，并且前四个是字母后8个是数字）
'''
def save():
    #定义一个空字符串用于拼接字符
    str_num = ''
    #循环前四个随机字母（用ASCII码对应的值随机转换成字母
    for i in range(4):
        num = random.randrange(97, 123)
        str_s = chr(num)#将数字转换成小写字母
        str_num = str_num + str_s#拼接成四个字母
    for i in range(8):
        num = random.randrange(0, 10)
        str_s = str(num)#将随机数转换成字符串
        str_num = str_num + str_s
    print(str_num)
#输入函数
num = input("请输入一个三位数：")#输入函数返回的是字符串，需要强制转换
#程序随机数
random_num = random.randrange(100,1000)
#检测输入的是否纯数字
if num.isdigit() and 100<= int(num)<=999:
    num = int(num)
    random_num = int(random_num)
    #判断输放的数与程序随机数的大小
    if num > random_num:
        bai = num //100
        shi = num %100 // 10
        ge = num % 10
        print("这个三位数的个位是{0},十位是{1},百位是{2}".format(ge, shi, bai))
    if num < random_num:
        save()
    if num == random_num:
        print("你中奖了",random_num)
else:
    print("请按规定输入：")

