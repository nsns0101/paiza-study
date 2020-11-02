import operator
array = input().split(" ")
# print(array)
ops = operator.add if(array[1] == "+") else operator.sub
# print(ops)
x_index = array.index('x')

# print(x_index)
result = 0
if(x_index == 0):
    result = int(array[2]) + int(array[4])
elif(x_index == 2):
    result = ops(int(array[4]), int(array[0]))
else:
    result = ops(int(array[0]), int(array[2]))
print(result)
