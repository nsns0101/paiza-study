
# 1:1 경기를 해서 승리, 패배에 대한 리그 테이블 작성하기
player = int(input()) # 플레이어 수
count = 0   # 게임 수(플레이어가 5명이면 4 + 3 + 2 + 1)
game = []   # 누구와 게임하고, 누가 이겼는지(앞 자리 배열이 승)
result = [] # 결과배열

for i in range(player -1, -1, -1):
    count+=i 
# print(count)

# 입력 받기
for i in range(0, count):
    game.append(input().split(" "))
# print(count)

# 빈 공간 만들기
for i in range(0, player):
    result.append([])
    for j in range(0, player):
        result[i].append('-')
# print(result)

# 경기 시작
for i in range(0, len(game)):
    for j in range(0, len(game)):
        if(i == j):
            continue
        else:
            result[int(game[i][0]) - 1][int(game[i][1]) - 1] = 'W'
            result[int(game[i][1]) - 1][int(game[i][0]) - 1] = 'L'
# print(result)


# 출력
for i in range(0, len(result)):
    print(' '.join(result[i]))
