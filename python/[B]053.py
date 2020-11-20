# H = 테이블의 행수 
# W = 테이블의 열수
H, W = input().split(" ")

a, b = input().split(" ")
c, d = input().split(" ")

H,W,a,b,c,d = int(H), int(W), int(a), int(b), int(c), int(d)


result = [ [a,b], [c, d] ]

W_add = b - a
H_add = c - a
# print("W_add", W_add)
# print("H_add", H_add)
for i in range(0, H):
    # print("i", i)
    if(i > 1):
        # result.append( result[i -1][0]+ (result[i -1][0] - result[i-2][0]) )

        result.append( [result[i -1][0]+ H_add] )
    
    for j in range(0, W):
        # print("result[i][j-1]", result[i][j-1])
        # print("RESULT", result)
        if( 
            (i == 0 and j == 0 ) or (i == 0 and j == 1 ) or
            (i == 1 and j == 0 ) or (i == 1 and j == 1 ) or j==0
        ):
            continue
        else:
            ono = (result[i-1][0] - result[i-2][0]) - (result[i-1][1] - result[i-2][1]) 
            print("ono", ono)
            # print("good", result[i][j-1] + W_add)
            # result[i].append( result[i][j-1] + (result[i][j -1] - result[i][j -2]) )
            result[i].append( result[i][j-1] + (W_add) - ono)

# print(len(result))

for i in range(0, H):
    print(" ".join(list(map(str, result[i]))))


# print(" ".join( list(map(str,result))))
