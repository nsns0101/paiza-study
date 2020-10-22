#넣을 자릿수의 개수, 숫자
input_line, input_line2 = input().split(" ")
input_line, input_line2 = int(input_line), int(input_line2)

number_count = []

# 입력
for i in range(0, input_line):
    number_count.append(int(input()))
    

result = []
while True:
    if(input_line2 <= 1):
        result.append(input_line2)
        break

    temp = input_line2 % 2  #나눴을때 나머지

    result.append(temp)
    input_line2 = int(input_line2 / 2)
    # print(input_line2)

# print(result)


for i in range(len(number_count)):
    print(result[number_count[i] - 1])

# 44 22 11 5 2 1




