N, c1, c2 = input().split(" ")
N, c1, c2 = int(N), int(c1), int(c2)

input_value = []
result = 0  # 이익, 손해
count = 0   # 주식 산 개수
for i in range(0, N):
    input_value.append( int(input() ))
    # 전부판매
    if(i == N - 1):
        result += (input_value[i] * count)
    # 구입
    elif(input_value[i] <= c1):
        result -= input_value[i]
        count += 1
    # 판매
    elif(input_value[i] >= c2):
        result += input_value[i] * count        
        count = 0
    
   
print(result)


