#포기
#R = 오른손 토글
#L = 왼손 토글
#N = 아무것도 하지않음

#game = 게임의 턴수
#k = 플레이어가 승리하는 성공 턴 수

game, k = input().split(" ")
game, k = int(game), int(k)

action = list(input())



#3 2
#RLN을 입력받을 경우(모두 위에 손)
# => NLR, NRL, LRN, NR