# m = 물건(kg)
# p 1차판매 %
# q 2차판매 %
# 남은 양 찾기
m,p,q = input().split(" ")
m,p,q = int(m), int(p), int(q)

m = m * ( ( 100 - p ) / 100 )
m = m * ( ( 100 - q ) / 100 )

print(m)

