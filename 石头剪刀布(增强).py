# 石头剪刀布5.0版(1.0版使用java进行制作)
import random as r
import time as t
import sys as s
input_error_number_of_times_1 = 0
input_error_number_of_times_2 = 0
computer_result = 0
human_result = 0
random = 0
type_in = 0
computer = [0, 1, 2, 2, 1, 0]
wait_time = 0
t.sleep(0.5)


def wait(output_character):
    print(output_character, end="")
    t.sleep(0.3)


wait("欢")
wait("迎")
wait("来")
wait("到")
wait("石")
wait("头")
wait("剪")
wait("刀")
wait("布")
print("4.0", end="")
t.sleep(0.3)
print("版")
while 1:
    if input_error_number_of_times_1 == 3:
        print("因为您输入错误数据次数过多,我们判定你有故意影响程序的嫌疑,所以程序将在3秒后关闭。")
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
        wait_time = float(input("在开始游戏之前，请输入AI出拳的速度(出拳速度跟实力无关)。\n"))
    except ValueError:
        print("请不要输入错误数据，谢谢!")
        input_error_number_of_times_1 += 1
    else:
        if 0 <= wait_time <= 30:
            break
        elif wait_time <= 0:
            print("数字过小!")
            input_error_number_of_times_1 += 1
        else:
            print("数字过大!")
            input_error_number_of_times_1 += 1
while 1:
    for i in range(10):
        print("请输入(0=石头,1=剪刀,2=布)。")
        while 1:
            if input_error_number_of_times_2 == 5:
                print("因为您输入错误数据次数过多,我们判定你有故意影响程序的嫌疑,所以程序将在3秒后关闭。")
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
                type_in = int(input())
            except ValueError:
                print("请勿输入错误数据，谢谢!")
                input_error_number_of_times_2 += 1
            else:
                if 0 == type_in < 3:
                    break
                elif type_in < 0:
                    print("数字过小!")
                    input_error_number_of_times_2 += 1
                else:
                    print("数字过大!")
                    input_error_number_of_times_2 += 1
        print("请等待电脑...")
        t.sleep(wait_time)
        random = r.choice(computer)
        print(random)
        if random == 0 and type_in == 0:
            print("你们打平了。")
            computer.append(2)
        elif random == 1 and type_in == 1:
            print("你们打平了。")
            computer.append(0)
        elif random == 2 and type_in == 2:
            print("你们打平了。")
            computer.append(1)
        elif random == 0 and type_in == 1:
            print("你输了...")
            computer.append(0)
            computer_result += 1
        elif random == 0 and type_in == 2:
            print("你赢了!")
            computer.append(1)
            human_result += 1
        elif random == 1 and type_in == 0:
            print("你赢了!")
            computer.append(2)
            human_result += 1
        elif random == 2 and type_in == 0:
            print("你输了...")
            computer.append(2)
            computer_result += 1
        elif random == 1 and type_in == 2:
            print("你输了...")
            computer.append(1)
            computer_result += 1
        elif random == 2 and type_in == 1:
            print("你赢了!")
            computer.append(0)
            human_result += 1
        else:
            print("输入错误")
    print("\n在这10局里:\n")
    print(f"电脑赢了{computer_result}局")
    print(f"你赢了{human_result}局")
    print(f"平了{10 - computer_result - human_result}局")
    if computer_result > human_result:
        print("电脑胜率比你高。\n")
    elif computer_result < human_result:
        print("你比电脑胜率高。\n")
    elif computer_result < human_result:
        print("你和电脑不相上下。\n")
    computer_result = 0
    human_result = 0
    input_error_number_of_times_2 = 0
