#编写程序，生成一个包含20个随机整数的列表，
# 然后对其中偶数下标（下标即列表元素的索引）的元素进行降序排列，
# 奇数下标的元素不变。（提示：使用切片。）
import random
list=[]
for i in range(1,21):
    list.append(random.randint(1,100))
list[::2]=sorted(list[::2],reverse=True)
print("元素降序排序",list)