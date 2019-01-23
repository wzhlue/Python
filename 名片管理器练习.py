from click._compat import raw_input

print("**********欢迎进入名片管理系统**********")

#用来存储学生信息
Students_List = []

def print_menu():
    print("1、添加学生信息")
    print("2、删除学生信息")
    print("3、修改学生信息")
    print("4、查询学生信息")
    print("5、展示学生信息")
    print("6、退出系统")


def add_new_std_infor():

    new_name = raw_input("请输入新的名字：")
    new_number = int(input("请输入新的学号："))
    new_cellphone = int(input("请输入新的手机号码："))
    new_address = raw_input("请输入新的地址：")

    new_infor ={}#定义一个新的字典，用来储存新的学生的信息
    new_infor['name'] = new_name
    new_infor['number'] = new_number
    new_infor['cellphone'] = new_cellphone
    new_infor['address'] = new_address

    #将一个字典添加到列表中
    Students_List.append(new_infor)     #用append函数在列表中加一个字典元素



def dele_std_infor():

    dele_name = input("请输入要删除的学生姓名：")
    find_flag = 0
    for temp in Students_List:
        if dele_name == temp['name']:
            find_flag =1
            Students_List.remove(temp)

            print("删除成功")
            break
    if find_flag == 0:
        print("没有要删除学生的信息")



def modify_std_infor():

    modify_name = raw_input("请输入要修改的学生名字：")
    modify_flag = 0
    for temp in Students_List:
        if modify_name == temp['name']:
            print("1、修改学生姓名")
            print("2、修改学生学号")
            print("3、修改学生电话")
            print("4、修改学生地址")
            print("5、退出修改系统")
            while True:
                num2 = int(input("请输入要修改的信息编号："))
                if num2 == 1:
                    temp['name'] =raw_input("请输入要修改的正确姓名：")
                    modify_flag = 1
                elif num2 ==2:
                    temp['number'] = int(input("请输入要修改的正确学号："))
                    modify_flag = 1
                elif num2 == 3:
                    temp['cellphone'] = int(input("请输入要修改的正确电话："))
                    modify_flag = 1
                elif num2 ==4:
                    temp['address'] = raw_input("请输入要修改的正确地址：")
                    modify_flag = 1
                elif num2 ==5:
                    break
                else:
                    print("输入有误，请重新输入")
                if modify_flag == 1:
                    print("修改成功")
                    break
            break



def find_std_infor():
    find_name =raw_input("请输入要查找的学生姓名：")

    find_flag = 0

    print("要查找的学生信息为：")
    print("姓名\t\t学号\t\t电话\t\t地址")

    for temp in Students_List:
        if find_name == temp['name']:
            print("%-12s%-12s%-12s%s"%(temp['name'],temp['number'],temp['cellphone'],temp['address']))
            find_flag = 1
        if find_flag == 0:
            print("没有找到这个学生")



def show_std_infor():
    #显示所有的学生信息
    print("姓名\t\t学号\t\t电话\t\t地址")
    for temp in Students_List:
        print("%-12s%-12s%-12s%s" % (temp['name'], temp['number'], temp['cellphone'], temp['address']))




def main():
    #管理整个系统
    print_menu()
    while True:
        num = int(input("请输入操作序号："))
        if num == 1:
            add_new_std_infor()
        elif num == 2:
            dele_std_infor()
        elif num == 3:
            modify_std_infor()
        elif num == 4:
            find_std_infor()
        elif num == 5:
            show_std_infor()
        elif num == 6:
            break
        else:
            print("输入有误，请重新输入")
        print("")

main()


