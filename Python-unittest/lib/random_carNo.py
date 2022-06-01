import random

def random_carNo(num,first='',second='',energy="tradition",cartype="small"):
    """
    随机生成车牌号，默认生成传统小型车车牌号
    :param num: 指定生成车牌号数量
    :param first: 指定车牌开头省份
    :param second: 指定车牌第二位
    :param energy: 汽车能源类型，传统能源（tradition），新能源（New）
    :param cartype: 车型大小，小型（small），大型（large）
    :return:
    """
    char0='京津沪渝冀豫云辽黑湘皖鲁新苏浙赣鄂桂甘晋蒙陕吉闽赣粤青藏川宁琼'
    char1='ABCDEFGHJKLMNPQRSTUVWXYZ'#车牌号中没有I和O，可自行百度
    char2='1234567890'
    len0 = len(char0)-1
    # print(len0)
    len1 = len(char1) - 1
    len2 = len(char2) - 1
    carNo=[]
    if energy=="tradition":
        for i in range(num):
            code = first+second+''
            index0 = random.randint(0, len0)
            index1 = random.randint(0, len1)
            if first=='':
                code += char0[index0]
            if second=='':
                code += char1[index1]
            for i in range(1, 6):
                index2 = random.randint(1, len2)
                code += char2[index2]
            carNo.append(code)
    elif energy=="New":
        for i in range(num):
            code = first+second+''
            index0 = random.randint(0, len0)
            index1 = random.randint(0, len1)
            if first=='':
                code += char0[index0]
            if second=='':
                code += char1[index1]
            if cartype=="small":
                for i in range(1, 7):
                    index2 = random.randint(1, len2)
                    if i == 1:
                        code += "D"
                    else:
                        code += char2[index2]
            elif cartype=="large":
                for i in range(1, 7):
                    index2 = random.randint(1, len2)
                    if i==6:
                        code+="D"
                    else:
                        code += char2[index2]
            carNo.append(code)
            # print(code)
    return carNo

# if __name__ == '__main__':
#     carNo=random_carNo(num=2)
#     print(carNo)
