#공격력, 방어력, 민첩함
ATK, DEF, AGI = input().split(" ")
#진화 수
N = int(input())

monster = []
no_count = 0
for i in range(0, N):
    monster.append(input().split(" "))
    # print(monster[i])
    if(
        int(monster[i][1]) <= int(ATK) and int(monster[i][2]) >= int(ATK) and
        int(monster[i][3]) <= int(DEF) and int(monster[i][4]) >= int(DEF) and
        int(monster[i][5]) <= int(AGI) and int(monster[i][6]) >= int(AGI) 
    ):
        print(monster[i][0])
    else:
        no_count+=1
    
    if(no_count == N):
        print("no evolution")

