input_num1, input_num2 = input().split(" ")
# input_num = list(map(int, input_num))
input_num1 = list(map(int, list(input_num1)))
input_num2 = list(map(int, list(input_num2)))

# print(input_num1, input_num2)

#앞에 0 추가
while True:
    if(len(input_num1) != 3):
        input_num1.insert(0, 0)
    elif(len(input_num2) != 3):
        input_num2.insert(0, 0)
    else:
        break
# print(input_num1, input_num2)

result = []
more_thousand = False

for i in range(0, len(input_num1)):
    if(input_num1[0] + input_num2[0] >= 10):
        more_thousand = True
    if(input_num1[i] + input_num2[i] >= 10):
        result.append( str(input_num1[i] + input_num2[i] - 10))
    else:
        result.append( str(input_num1[i] + input_num2[i]))

# if(more_thousand):
#     print(result)
if(more_thousand == False and result[0] == '0'):
    result.pop(0)

# good = 0
# for i in range(0, len(result)):
#     good += result[i] * ( 10 ** ( len(result) -1 - i))

# print(good)

print(''.join(result))