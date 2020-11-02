# 문제 이해가 안됨
day_length = int(input())

day = input().split(" ")
day = list(map(int, day))

for i in range (len(day), 14):
    day.append(1)
# print(day)
good = 0
result_count = 0

for i in range(0, 14):
    count = 0
    for j in range(0, 7):
        if(i + j >= 14):
            good = i + j - 14
            # print(good)
        else:
            good = i + j
        
        # print(good)
        if(day[good] == 0):
            count+=1
            # print("good")
    if(count >= 2):
        result_count+=1
    # print("----------------")
print(result_count)


# for i in range(0, day_length):
#     count = 0
#     for j in range(0, 7):
#         if(i + j >= day_length):
#             good = i + j - day_length
#             # print(good)
#         else:
#             good = i + j
        
#         print(good)
#         if(day[good] == 0):
#             count+=1
        
#     if(count == 2):
#         result_count+=1
#     print("----------------")
# print(result_count)

