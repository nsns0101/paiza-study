# rstrip = 문자열의 끝을 삭제

N = int(input())
if N == 0:
    exit()

result = []
for i in range(N):
    w = input()
    if w[-1] == 's' or w[-2:] == 'sh' or w[-2:] == 'ch' or w[-1] == 'o' or w[-1] == 'x'  :
        result.append(w + 'es')

    elif w[-1] == 'f' or (w[-1] == 'e' and w[-2] == 'f'):
        if w[-1] == 'e':
            result.append(w.rstrip('fe') + 'ves')
        else:
            result.append(w.rstrip('f') + 'ves')


    elif w[-2] != 'a' and w[-2] != 'i' and w[-2] != 'u' and w[-2] != 'e' and w[-2] != 'o' and w[-1] == 'y':
        result.append(w.rstrip('y') + 'ies')

    else:
        result.append(w + 's')

for i in range(len(result)):
    print(result[i])
