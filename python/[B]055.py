# N = 택시의 종류 수
# X = 목적지까지의 거리
N, X = input().split(" ")
N, X = int(N), int(X)

# 택시 기본 요금 거리, 기본 요금, 가산 거리, 부과 요금

taxi = []
for i in range(0, N):
    taxi.append(input().split(" "))
    taxi[i] = list(map(int, taxi[i]))

result = []
for i in range(0, len(taxi)):
    #기본요금거리보다 이동거리가 적을 때
    if(X - taxi[i][0] < 0):
        result.append( taxi[i][1] )
    #기본요금거리보다 이동거리가 많을 때
    else:
        korea = 0 # 총 가산거리
        okane = 0 # 총 부과요금

        #목적지까지의 거리 > (기본 이동거리 + 가산 거리)
        while X >= ( taxi[i][0] + korea ):
            korea += taxi[i][2]
            okane += taxi[i][3]
        result.append( taxi[i][1] + okane )

# print(result)
# print(" ".join( list(map(str,result))))
print (min(result), max(result))
# print(taxi)



# 2 700
# 600 200 200 400
# 900 800 400 500을 입력받으면

# 700m를 이동할 경우

# 1
# 700m - 기본요금 거리(600m, 200엔) = 100m를 더 이동해야 함
# 0~200m(가산거리)를 이동할때 부과요금이 400엔이니까
# 200엔 + 400엔 = 600엔
 
# 2
# 700m - 기본요금 거리(900m, 800엔) = 기본 요금 거리 미만
# = 800엔 