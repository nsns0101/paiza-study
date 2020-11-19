n = int(input())
# 계산하는 횟수
num1 = 0
num2 = 0

cul = []

for i in range(0, n):
    cul.append(input().split(" "))

    #SET
    if("SET" in cul[i]):
        if(cul[i][1] == "1"):
            num1 = int(cul[i][2])
        else:
            num2 = int(cul[i][2])
    #ADD
    elif("ADD" in cul[i]):
        num2 = num1 + int(cul[i][1])
    #SUB
    else:
        num2 = num1 - int(cul[i][1])

print(num1, num2)