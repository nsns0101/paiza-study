# n = 날의 개수
# 시가, 종가, 고가, 저가 찾기
n = int(input())

date = []
for i in range(0, n):
    date.append( input().split(" ") )
    date[i] = list(map(int, date[i]))

# print(date)

#고가
max_date = []
#저가
min_date = []

for i in range(0, n):
    max_date.append( date[i][2] )
    min_date.append( date[i][3] )


result = []

#시가
result.append(date[0][0])
#종가
result.append(date[n-1][1])
#고가
result.append(max(max_date))
#저가
result.append(min(min_date))

print(" ".join( list(map(str,result))))
