# X = 커피 가격
# P = 할인 비율
x, p = input().split(" ")
x, p = int(x), int(p)

count = 0
result = 0
while x != 0:
    result += x
    x = int(x - (x / ( 100 / p )))

print(result)
