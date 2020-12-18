#제일 높은자리 수와 낮은 자리수가 대칭되게 만드는 것
#대칭되지않으면 수를 반전시켜 더하기
# ex ) 261을 입력
# 261 + 162 = 423 ===> 대칭x  ==> 계속 실행
# 423 + 324 = 747 ===> 대칭o
# 정답은 747
input_value = int(input())

#대칭 값이 아니면 값을 반대로하여 두 수를 더해 반환
def digit_reverse(number):
    change_number =  [i for i in str(number)][::-1]

    return number + int(''.join(change_number))

while(True):
    input_value = digit_reverse(input_value)
    # print(input_value)
    if(list(str(input_value))[0] == list(str(input_value))[-1]):
        break

print(input_value)





