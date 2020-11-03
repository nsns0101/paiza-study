# M = 입 후보자의 수
# N = 유권자의 수
# K = 연설 횟수
# 가장 지지자가 많은 후보 출력
# 연설을 하면 다른 후보자의 유권자와 N에서 1명을 뺏어올 수 있음
M, N, K = input().split(" ")
M, N, K = int(M), int(N), int(K)

# 입후보자 별 보유하는 유권자 수
people = []
for i in range(0, M):
    people.append(0)

#연설하는 입 후보자 번호
speech_num = []
for i in range(0, K):
    speech_num.append( int(input()) )

# 유권자 뺏기 연설
for i in range(0, K):
    #N 유권자 뺏기
    if(N > 0):
        people[speech_num[i] - 1]+=1
        N-=1

    # people[i-1] 부터 뺏어야 하고
    # people[i+1] 부터 뺏어야 함
    for j in range(0, len(people)):
        # 내 유권자말고 1명씩 뺏기
        if(i != j):
            # 유권자가 0인 사람은 뺏을 수 없음
            if(people[j] <= 0):
                people[j] = 0
            # 유권자를 보유하고 있는 후보자의 유권자 뺏기
            else:
                people[j]-=1
                people[speech_num[i] - 1]+=1
    # print(people)
# print(people)

#가장 많은 유권자 수를 가진 후보자들 찾기
for i in range(0, len(people)):
    if(people[i] == max(people)):
        print(i+1)


# EX) 
#3 3 4
#1
#1
#2 을 입력할 경우
# 1번 연설자 1   2번 연설자 0   3번 연설자 0     N(유권자) = 2
# 1번 연설자 2   2번 연설자 0   3번 연설자 0     N(유권자) = 1
# 1번 연설자 1   2번 연설자 2   3번 연설자 0     N(유권자) = 0
# 1번 연설자 0   2번 연설자 1   3번 연설자 2     N(유권자) = 0  