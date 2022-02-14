import csv
import random

f = csv.reader(open('1.csv', 'r', encoding='UTF-8-sig'))
dict_1 = []
for i in f:
    dict_1.append(i)
sum = 0
power = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]  # 加权因子
check = [1, 0, 10, 9, 8, 7, 6, 5, 4, 3, 2]  # 校验码，10代表X
area = random.randrange(0, 3211)  # 随机抽个地区
year = random.randrange(1960, 2001)  # 保证成年，我就写了1960到2000的
month = random.randrange(10, 13)  # 懒得补0，直接取10月到12月
day = random.randrange(10, 29)  # 懒得补0和判断大小月，直接取10号到28号
num = random.randrange(100, 1000)  # 同上，直接取100到999
a = dict_1[area][0] + str(year) + str(month) + str(day) + str(num)  # 生成前17位
for i in range(0, 17):
    sum += int(a[i]) * power[i]  # 17位乘以对应加权因子，求和
b = str(check[sum % 11])  # 求余数
if b == 10:  # 把第18位加上
    a = a + 'X'  # 把10变成X
else:
    a = a + b
print(a)
