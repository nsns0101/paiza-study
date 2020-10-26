# H = 입력 문자열 길이
# W = 상자의 원래 길이
# X = 상자의 수정할 길이
H, W, X = input().split(" ")
H, W, X = int(H), int(W), int(X)

input_word = []
result = ""
for i in range(0, H):
    input_word.append(input())
    result += input_word[i]

# print(len(result))
# print("\n")

# 5 11 17 23
count = 1
n_index = []
for i in range(0, len(result)):
    if( i % X - 5 == 0):
        # n_index.append(i)
        if( count == 1):
            result = result[: X*count] + '\n' + result[X*count:]
            count += 1
        else:
            result = result[: X*count + count - 1] + '\n' + result[X*count + count - 1:]
            count += 1


# print(len(result))
print(result)


