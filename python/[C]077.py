# k = 인원수
# n = 문제
k, n = input().split(" ")
k, n = int(k), int(n)

score = []
result_value = []

# 입력
for i in range(0, k):
    score.append(input().split(" "))

# 점수 계산
for i in range(0, len(score)):
    result_value.append ((100 / n) * int(score[i][1]))
    
    if ( int(score[i][0]) >= 10):
        result_value[i] = "D"
        continue
    elif( int(score[i][0]) >= 1):
        result_value[i] *= 0.8

    
    if(result_value[i] >= 80):
        result_value[i] = "A"
    elif(result_value[i] >= 70):
        result_value[i] = "B"
    elif(result_value[i] >= 60):
        result_value[i] = "C"
    else:
        result_value[i] = "D"

for i in range(0, len(result_value)):
    print(result_value[i])

