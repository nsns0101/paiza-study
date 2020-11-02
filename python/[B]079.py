s, t = input().split(" ")

arr_name = list(s + t)

# print(arr_name)

result = []
for count in range(0, 2):
    value = []

    # 앞 이름 + 뒤 이름
    if(count == 0):
        arr_name = list(s + t)
    # 뒤 이름 + 앞 이름
    else:
        arr_name = list(t + s)
    # print(arr_name)


    for i in range(0, len(arr_name)):
        #ascii code - 96 => 'a'를 1로, 'z'를 26으로
        value.append( ord(arr_name[i]) - 96)
    # print(value)

    for i in range(0, len(value)):
        for j in range(0, len(value) - 1):
            # print(value)
            value[j] = value[j] + value[j + 1]
            
            # 101을 넘으면 초기화
            if(value[j] > 101):
                value[j]-=101
        if(len(value) >= 2):
            # print( len(value) )
            del value[len(value) - 1]
    result.append(value[0])
    # print(result)

    
if(result[0] > result[1]):
    print(result[0])
else:
    print(result[1])
    
