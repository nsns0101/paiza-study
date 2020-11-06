temp_arr = []
result = []
for i in range(0, 10):
    # 짝수 번 실행일 때 
    if( i % 2 == 0):
        #초기화 전에 temp_arr값을 result에 저장하고
        result.append(temp_arr)

        #temp_arr배열을 초기화
        temp_arr.clear()
        # temp_arr = []
    
    # temp_arr에 i 대입 
    temp_arr.append(i)

    print("result => ", result)

print("출력 => ", result)
# 예상값 [ [0,1], [2,3], [4,5], [6,7], [8,9] ]
# 출력값 [ [8,9], [8,9], [8,9], [8,9], [8,9] ]
# => 출력값이 이렇게 되는 이유가 궁금합니다.