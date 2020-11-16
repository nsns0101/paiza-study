#미 해결
input_line1, input_line2, input_line3 = input().split(" ")

str_length, original_arr, change_arr = int(input_line1), list(input_line2), list(input_line3)
# print(original_arr, change_arr)

temp_arr = []

for i in range(0, str_length):
    if original_arr[0] == change_arr[i]:
        temp_arr.append(i)

print(temp_arr)
temp_count = 0  
complated_count = 0 

# for i in range(0, str_length):
i = 0
while i < str_length:
    print(i, str_length)
    ch_num = i
    if temp_arr[temp_count] + ch_num >= str_length :
        ch_num = ch_num + temp_arr[temp_count] - str_length
    # print(ch_num)
    # print(original_arr[ch_num], change_arr[temp_arr[temp_count] + ch_num])

    if original_arr[ch_num] == change_arr[temp_arr[temp_count] + ch_num] :
        # print("complated_count++")
        complated_count+=1
    else :
        complated_count = 0
        temp_count+=1
        i = 0
        # print("good")

    # print(str_length, complated_count)
    if(str_length== complated_count):
        print(temp_arr[temp_count])

    i+=1
    # print(i)

# 0에서 length까지 반복
# 문자열1[0]과 문자열2[i]가 같은지 비교
# 같은게 나왔다면
# ex) ABCABD, BDABCA라면
# 문자열1[0]과 문자열2[2], 문자열[5]와 같음
# temp_arr = [2,5]

# 같을시 count++
# 문자열1[temp[0] + 0]과 문자열2[2] 비교  count = 1
# 문자열1[temp[0] + 1]과 문자열2[3] 비교  count = 2
# 문자열1[temp[0] + 2]과 문자열2[4] 비교  count = 3
# 문자열1[temp[0] + 3]과 문자열2[5] 비교  count = 4
# 문자열1[temp[0] + 4]과 문자열2[0] 비교  count = 5
# 문자열1[temp[0] + 5]과 문자열2[1] 비교  count = 6
# => 문자열[temp[0] + i]과 문자열2[i+2]
# if( i + 2 >= 문자열길이)라면 i + 2 - 문자열길이(6)을 함  

# 문자열 길이와 count가 같으면 성공
# 아니면 문자열[5]부터 다시 함