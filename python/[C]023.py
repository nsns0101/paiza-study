#good_number = 당첨번호
#count = 복권 개수
good_number = input().split(" ")
count = int(input())

#challenge_number = 산 복권
challenge_number = []
for i in range(0, count):
    challenge_number.append(input().split(" "))

result = []
#당첨번호와 산 복권 비교
for i in range(0, count):
    good_count = 0
    for j in range(0, 6):
        if( challenge_number[i][j] in good_number):
            good_count+=1
    result.append(good_count)

for i in range(0, len(result)):
    print(result[i])