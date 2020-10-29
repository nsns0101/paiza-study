# 왜 20점?
# N = 가게 수
# M = 자신 이외의 사용자 수
# K = 자신과 취향이 비슷하다고
N, M, K = input().split(" ")
N, M, K = int(N), int(M), int(K)

good = []
for i in range(0, M+1):
    # 자신 이외의 사용자 수 + 자신 수 만큼
    # for j in range(0, M + 1):
    good.append( input().split(" "))
    good[i] = list(map(int, good[i]))

# print(good)
# print("\n")

result = []
for i in range(0, N):
    good_count = 0
    
    # 가본적 없는 가게에 가고 싶음
    if(good[0][i] != 0):
        continue
    
    for j in range(0, M+1):

        # 별 3점이면
        if(good[j][i] == 3):
            good_count+=1
    # 별 3점 리뷰가 K개 이상이면
    if(good_count == K):
        result.append(i+1)

if(result):
    print(" ".join( list(map(str,result))))
else:
    print("no")