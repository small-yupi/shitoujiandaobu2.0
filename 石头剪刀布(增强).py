# 石头剪刀布5.0版(1.0版使用java进行制作)
# 模块导入
import random as r
import time as t
import sys as s
# 定义变量
# 记录错误数据变量:
input_error_number_of_times_1 = 0
input_error_number_of_times_2 = 0
input_error_number_of_times_3 = 0
# 记录电脑和用户所有战绩、局数变量:
all_computer_result = 0
all_human_result = 0
board_number = 0
draw = 0
# 判断是否要查看电脑和用户所有战绩变量:
judge_check_total_score = 0
# 记录10局里电脑和用户所有战绩变量:
computer_result = 0
human_result = 0
# 电脑随机结果变量:
random = 0
# 用户输入变量:
type_in = 0
# 电脑随机数据变量:
computer = [0, 1, 2, 2, 1, 0]
# 电脑出拳等待时间变量:
wait_time = 0
# 等待
t.sleep(0.5)
# 定义函数
# 开场动画函数:


def popping_character(output_character):
    print(output_character, end="")
    t.sleep(0.3)


# 设置开场动画
popping_character("欢")
popping_character("迎")
popping_character("来")
popping_character("到")
popping_character("石")
popping_character("头")
popping_character("剪")
popping_character("刀")
popping_character("布")
print("4.0", end="")
t.sleep(0.3)
print("版")
# 开场设置
while 1:
    # 设定多次输入错误数据的结果
    if input_error_number_of_times_1 == 3:
        print("因为您输入错误数据次数过多, 我们判定你有故意影响程序的嫌疑, 所以程序将在3秒后关闭。")
        print("3")
        t.sleep(1)
        print("2")
        t.sleep(1)
        print("1")
        t.sleep(1)
        print("0")
        print("程序已结束")
        s.exit(0)
    # 防止程序报错 "ValueError"
    try:
        wait_time = float(input("在开始游戏之前, 请输入AI出拳的速度(出拳速度跟实力无关)。\n"))
    # 引发错误 "ValueError" 后提示
    except ValueError:
        print("请不要输入错误数据, 谢谢!")
        input_error_number_of_times_1 += 1
    # 判断数字是否在正常范围内
    else:
        if 0 <= wait_time <= 30:
            break
        elif wait_time <= 0:
            print("数字过小!")
            input_error_number_of_times_1 += 1
        else:
            print("数字过大, 为了您的体验, 请将数字调小。")
            input_error_number_of_times_1 += 1
# 开始石头剪刀布
while 1:
    # 10次为一个周期
    for i in range(10):
        print("请输入(0=石头,1=剪刀,2=布)。")
        # 选择选项
        while 1:
            # 设定多次输入错误数据的结果
            if input_error_number_of_times_2 == 5:
                print("因为您输入错误数据次数过多, 我们判定你有故意影响程序的嫌疑, 所以程序将在3秒后关闭。")
                print("3")
                t.sleep(1)
                print("2")
                t.sleep(1)
                print("1")
                t.sleep(1)
                print("0")
                print("程序已结束")
                s.exit(0)
            # 防止出现错误 "ValueError"
            try:
                type_in = int(input())
            # 引发错误 "ValueError" 后提示
            except ValueError:
                print("请勿输入错误数据, 谢谢!")
                input_error_number_of_times_2 += 1
            # 判断数字是否在正常范围内
            else:
                if 0 == type_in < 3:
                    break
                elif type_in < 0 or type_in > 2:
                    print("不存在此选项")
                    input_error_number_of_times_2 += 1
        print("请等待电脑...")
        # 等待
        t.sleep(wait_time)
        # 电脑出拳随机
        random = r.choice(computer)
        print(random)
        # 判断胜负并根据用户出拳更改出拳概率
        if random == 0 and type_in == 0:
            print("你们打平了。")
            computer.append(2)
            draw += 1
        elif random == 1 and type_in == 1:
            print("你们打平了。")
            computer.append(0)
            draw += 1
        elif random == 2 and type_in == 2:
            print("你们打平了。")
            computer.append(1)
            draw += 1
        elif random == 0 and type_in == 1:
            print("你输了...")
            computer.append(0)
            computer_result += 1
            all_computer_result += 1
        elif random == 0 and type_in == 2:
            print("你赢了!")
            computer.append(1)
            human_result += 1
            all_human_result += 1
        elif random == 1 and type_in == 0:
            print("你赢了!")
            computer.append(2)
            human_result += 1
            all_human_result += 1
        elif random == 2 and type_in == 0:
            print("你输了...")
            computer.append(2)
            computer_result += 1
            all_computer_result += 1
        elif random == 1 and type_in == 2:
            print("你输了...")
            computer.append(1)
            computer_result += 1
            all_computer_result += 1
        elif random == 2 and type_in == 1:
            print("你赢了!")
            computer.append(0)
            human_result += 1
            all_human_result += 1
    # 记录局数
    board_number += 10
    # 展示在这10局里双方战绩
    print("\n在这10局里:\n")
    print(f"电脑赢了{computer_result}局")
    print(f"你赢了{human_result}局")
    print(f"平了{10 - computer_result - human_result}局")
    # 判断双方胜率高低
    if computer_result > human_result:
        print("电脑胜率比你高。\n")
    elif computer_result < human_result:
        print("你比电脑胜率高。\n")
    elif computer_result < human_result:
        print("你和电脑不相上下。\n")
    t.sleep(1)
    # 判断用户要不要查看用户和电脑的所有战绩
    while 1:
        if input_error_number_of_times_3 == 2:
            print("因为您输入错误数据次数过多, 我们判定你有故意影响程序的嫌疑, 所以程序将在3秒后关闭。")
            print("3")
            t.sleep(1)
            print("2")
            t.sleep(1)
            print("1")
            t.sleep(1)
            print("0")
            print("程序已结束")
            s.exit(0)
        try:
            judge_check_total_score = int(input("你要不要查看你和电脑的所有战绩(0=不要, 1=要)\n"))
        except ValueError:
            print("请不要输入错误数据, 谢谢!")
            input_error_number_of_times_3 += 1
        else:
            if judge_check_total_score == 0 or judge_check_total_score == 1:
                break
            else:
                print("没有此选项")
                input_error_number_of_times_3 += 1
    # 展示双方所有战绩
    print(f"\n在这{board_number}局里:\n")
    print(f"电脑赢了{all_computer_result}局")
    print(f"你赢了{all_human_result}局")
    print(f"平了{draw}局")
    # 判断双方胜率高低
    if all_computer_result > all_human_result:
        print("电脑胜率比你高。\n")
    elif all_computer_result < all_human_result:
        print("你比电脑胜率高。\n")
    elif all_computer_result < all_human_result:
        print("你和电脑不相上下。\n")
    # 变量初始化
    computer_result = 0
    human_result = 0
    input_error_number_of_times_2 = 0
