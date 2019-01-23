# nameList =["张三","李四","王五"]
# findName =input('请输入要查找的姓名')
#
#
# if findName in nameList:
#     print('列表中有这个人')
# else:
#     print('查无此人')

# movieName = ['加勒比海盗','骇客帝国','第一滴血','指环王','霍比特人','速度与激情']

#del    根据下标删除元素
# print('------删除之前------')
# for tempName in movieName:
#     print(tempName)
#
# del movieName[2]
#
# print('------删除之后------')
# for tempName in movieName:
#     print(tempName)

#pop删除最后一个元素
# movieName.pop()
#
# for tempName in movieName:
#     print(tempName)

#根据元素的值进行删除
# movieName.remove('第一滴血')
#
# for tempName in movieName:
#     print(tempName)

# number_List =[8,3,4,2,6,5,7]
# #reverse 逆序排列
# #number_List.reverse()
#
# #sort   按照某种顺序排列，默认是从小到大
# number_List.sort()
#
# print(number_List)

#encoding=utf-8

#import random
#
# # 定义一个列表用来保存3个办公室
# offices = [[],[],[]]
#
# # 定义一个列表用来存储8位老师的名字
# names = ['A','B','C','D','E','F','G','H']
#
# i = 0
# for name in names:
#     #random.randint(): 随机生成一个int类型的数，可以指定这个数的范围
#     index = random.randint(0,2)
#     offices[index].append(name)
#
# i = 1
# for tempNames in offices:
#     print('办公室%d的人数为:%d'%(i,len(tempNames)))
#     i+=1
#     for name in tempNames:
#         print("%s"%name,end='')
#     print("\n")
#     print("-"*20)

# import random
#
# offices = [[],[],[]]
#
# teacher_Name =["A","B","C","D","E","F","G"]
#
# for name in teacher_Name:
#     index = random.randint(0,2)
#     offices[index].append(name)
#
# i = 1
# for tempName in offices:
#     print('办公室%d的人数为：%d'%(i,len(tempName)))
#     i += 1
#     for name in tempName:
#         print('%s'%name,end='')
#     print("\n")
#     print('-'*20)

#给定一个字符串，反转它

# Str = "abcdefg"
# newStr = Str[::-1]
# print(newStr)


dict = {"name":'张三','age':18,'address':'安徽滁州'}

# #遍历元素值
# for value in dict.values():
#     print(value)
#
# #遍历键
# for key in dict.keys():
#     print(key)
#
# #遍历键值对
# for item in dict.items():
#     print(item)

#带下标索引的遍历
for i,dic in enumerate(dict):
    print('%d %s' %(i,dic))