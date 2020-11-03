# 문제 이해가 안됨
day_length = int(input())

day = input().split(" ")
day = list(map(int, day))

# for i in range (len(day), 14):
#     day.append(1)
# print(day)
good = 0
result_count = 0
for i in range(0, day_length):
    minus_count = 1
    count = 0
    # end_start_count = 0
    for j in range(0, 7):

        # if(i + j == 0):
        #     print("시작")
        #     end_start_count+=1
        # elif(i + j == day_length - 1):
        #     print("끝")
        #     end_start_count+=1


        if(i + j >= day_length):
            # good = i + j - 14
            good = i - minus_count
            minus_count+=1
            print("if" , i, j, good)
        else:
            good = i + j
            print("else" , i, j, good)
        
        # print(good)
        if(day[good] == 0):
            count+=1
            print("쉬는날")

    if(count >= 2):
        result_count+=1
    print("----------------")
print(result_count)