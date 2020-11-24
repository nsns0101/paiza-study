
player_arr = []
player_arr.append(input().split(" "))
player_arr.append(input().split(" "))

e_arr = []
e_arr.append(input().split(" "))
e_arr.append(input().split(" "))



for i in range(0, 2):
    for j in range(0, 2):
        if(player_arr[i][j] == '1'):
            player_arr[i].append(e_arr[0][0])
        elif(player_arr[i][j] == '2'):
            player_arr[i].append(e_arr[0][1])
        elif(player_arr[i][j] == '3'):
            player_arr[i].append(e_arr[0][2])
        elif(player_arr[i][j] == '4'):
            player_arr[i].append(e_arr[0][3])

good_player = []

if(player_arr[0][2] > player_arr[0][3]):
    good_player.append( [player_arr[0][1], e_arr[1][0]] )
else:
    good_player.append( [player_arr[0][0], e_arr[1][0]] )

if(player_arr[1][2] > player_arr[1][3]):
    good_player.append( [player_arr[1][1], e_arr[1][1]] )
else:
    good_player.append( [player_arr[1][0], e_arr[1][1]] )

# print(good_player)

result = [0, 0]
if( max(e_arr[1]) == good_player[0][1]):
    result[0] = good_player[0][0]
    result[1] = good_player[1][0]
else:
    result[0] = good_player[1][0]
    result[1] = good_player[0][0]

for i in range(0, 2):
    print(result[i])



