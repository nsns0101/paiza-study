# N = N * N의 테이블
# 세로, 가로 대각선 줄의 합이 모두 같게할 때 넣어야할 값은?
    # EX 입력)
        # 3
        # 6 1 8
        # 7 5 3
        # 2 0 0
# => 0의 자리에 값을 넣고 올바른 테이블 리턴하기
N = int(input())

# N * N 테이블 생성
table = [[int(m) for m in input().split(" ")] for _ in range(N)]

# 테이블의 열, 행, 대각선 값의 합을 구하기
# 3 * 3 테이블이면
# s = 3 * (3의 2제곱 + 1) / 2 의 몫
s = N * (N ** 2 + 1) // 2

# 0이 있는 인덱스 찾기
z = []
for i,i_v in enumerate(table):
    for j,j_v in enumerate(i_v):
        if j_v == 0:
            z.append((i,j))

# zi1, zj1, zi2, zj2에 저장
zi1, zj1 = z[0]
zi2, zj2 = z[1]

# 0이 없는 행, 열에서 s - 값
if zi1 != zi2:
    table[zi1][zj1] = int(s) - sum([table[zi1][j] for j in range(N)])
    table[zi2][zj2] = int(s) - sum([table[zi2][j] for j in range(N)])
elif zj1 != zj2:
    table[zi1][zj1] = int(s) - sum([table[i][zj1] for i in range(N)])
    table[zi2][zj2] = int(s) - sum([table[i][zj2] for i in range(N)])

# 테이블 출력
for row in table:
    print(' '.join(map(str, row)))