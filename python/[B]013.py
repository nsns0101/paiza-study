#100점 29분
# a = 집에서 역까지 걸리는 시간
# b = 역에서 환승역까지 걸리는 시간
# c = 환승역에서 회사까지의 시간
# N = 처음 역에 기차가 오는 횟수
a, b, c = input().split(" ")
a, b, c = int(a), int(b), int(c)
N = int(input())

# h = 처음 역에서 기차가 출발하는 시간
h = []
for i in range(0, N):
    # 시, 분
    h.append( input().split(" "))
    h[i] = list(map(int, h[i]))

    #분 단위로 바꾸기
    h[i] = h[i][0] * 60 + h[i][1] * 1
# print(h)

result = ""

for i in range(N - 1, -1, -1):
    # print(h[i])
    # 9시간(630분)미만으로 들어갈 수 있나?
    if(540 > h[i] + b + c):
        # print(h[i] + b + c)
        result = h[i] - a
        break
result_h = int(result / 60)
result_m = result % 60

if(result_h < 10):
    result_h = "0" + str(result_h)
if(result_m < 10):
    result_m = "0" + str(result_m)

print( str(result_h) + ":" + str(result_m) )
# if(result >= 600):
            



