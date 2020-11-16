# N 각 영수증의 수
N = int(input())

input_value = []
for i in range(0, N):
    input_value.append(input().split(" "))
    

point = 0
for i in range(0, len(input_value)):
    # if(list(input_value[i][0])[-1] == 3 or list(input_value[i][0])[-1] == 5):
        # point += int( int(input_value[i][1]) / (100 * list(input_value[i][0])[-1]))
    if "3" in list(input_value[i][0]):
        # print("3")
        point += int( int(input_value[i][1]) * 3 / 100)
    elif "5" in list(input_value[i][0]):
        # print("5")
        point += int( int(input_value[i][1]) * 5 / 100)
    else:
        # print("else", int( int(input_value[i][1]) / 100))
        point += int( int(input_value[i][1]) / 100)

print(point)