# M = 요리의 종류 수
# N = 학생 수

M, N = input().split(" ")
M, N = int(M), int(N)

# 각각의 식품 칼로리
food_kcal = []

for i in range(0, M):
    food_kcal.append(input())

food_kcal = list(map(int, food_kcal))
# print("---------------")
# print(food_kcal)

# 각각의 학생들이 먹은 칼로리
N_kcal = []

for i in range(0, N):
    N_kcal.append( input().split(" "))
    N_kcal[i] = list(map(int, N_kcal[i]))
# print(N_kcal)

#  식품 칼로리[i]  * (먹은칼로리[i] / 100)

result = []
for i in range(0, N):
    value = 0
    for j in range(0, M):
        value += int(food_kcal[j] * (N_kcal[i][j] / 100))
    result.append(value)


for i in range(0, len(result)):
    print(result[i])