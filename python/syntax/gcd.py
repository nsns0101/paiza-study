numA = input("first : ")
numB = input("second : ")

try:
    numA = int(numA)
except:
    print("numA is not an integer")
    numA = input("first : ")
try:
    numB = int(numB)
except:
    print("numB is not an integer")
    numB = input("first : ")


lst = []
big = max(numA, numB)
for i in range(1, big + 1):
    if(numA % i == 0 and numB % i == 0):
        lst.append(i)
        print("GCD : ", max(lst))
        break