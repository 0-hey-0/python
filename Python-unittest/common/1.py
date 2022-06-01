import random
# print(random.randint(10,99))

# for i in range(0,1):
#     print(i)

#
# P_num_list=[]
# for num in range(0,30):
#     for i in range(2,num):
#         if num%i==0:
#             break
#     else:
#         P_num_list.append(num)
# print("0-30质数是：",P_num_list)



# num = input('请输入4位的正整数：')
# # 2、求和
# s = '+'.join(num)  # '1+2+3+4'
# # print(f'{num}每一位上数字的和为：{eval(s)}')  # eval()，接收一个字符串，可以对这个字符串进行运算
# print("%s每一位上数字的和为：%d"%(num,eval(s)))

#
import random
def chepaihao():
  char0='京津沪渝冀豫云辽黑湘皖鲁新苏浙赣鄂桂甘晋蒙陕吉闽赣粤青藏川宁琼'
  char1='ABCDEFGHJKLMNPQRSTUVWXYZ'#车牌号中没有I和O，可自行百度
  char2='1234567890'
  len0 = len(char0) - 1
  len1 = len(char1) - 1
  len2 = len(char2) - 1
  while True:
    code = ''
    index0 = random.randint(1,len0 )
    index1 = random.randint(1, len1)
    code += char0[index0]
    code += char1[index1]
    for i in range(1, 6):
      index2 = random.randint(1, len2)
      code += char2[index2]
    print(code)
if __name__=='__main__':
  chepaihao()


# char0='京津沪渝冀豫云辽黑湘皖鲁新苏浙赣鄂桂甘晋蒙陕吉闽赣粤青藏川宁琼'
# i=random.randint(1,len(char0))
# print(char0[i])

# list=[1,2,3,4]
# it=iter(list)
#
# for i in it:
#     print(i,end=" ")


# a,b = 10,20
# c = 1
# print(a > 10 and (c:=b>10))  # 左边表达式结果为False，则右边的表达式不会再运行，则c的值不变
# print(c)   # 1
# print(a >= 10 or (c:=b>10))  # 左边表达式结果为True，则右边的表达式不会再运行，则c的值不变
# print(c)   # 1


#
# from selenium import webdriver
#
#
# driver=webdriver.Chrome()
# driver.get("http://www.baidu.com")


# import re
#
# # print(re.split('\W+', 'runoob, runoob, runoob.'))
# print(re.split('(\W+)',' runoob, runoob, runoob.'))

# import calendar
#
# cal = calendar.month(2022, 4)
# print ("以下输出2022年4月份的日历:")
# print (cal)


import re


# str="xxx出生于2002年5月1日"
# str="xxx出生于2002年05月01日"
# str="xxx出生于2002-5-1"
# str="xxx出生于2002-05-01"
# str="xxx出生于2002-05"
# str="xxx出生于2002/5/1"
# str="xxx出生于20020501"
# str="xxx出生于20020501"
#
# regex_str=".*出生于(\d{4}[年/-]\d{1,2}([月/-]\d{1,2}(日|$)|[月/-]$|$)|\d{8})"
# match_str=re.match(regex_str,str)
# print(match_str)
# if match_str:
# #     print(match_str.group(1)
# import time
#
# time.sleep(5)



