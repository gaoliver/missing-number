import math

array = [-20000, -0.0003, 0, -0.0005, 1, 1.003, 0.003, 5, 500000] # Edit this array the way you want

def reducer(A):
    x = []
    A.sort()
    for i in A:
        if i not in x:
            x.append(i)
    return x

def solution(A):
    B = reducer(A)

    x = 0

    for y in B:
        x += 1

        if ((max(B) == y) and (y > 0)):
            if (y < 1):
                print("_1_")
                return math.ceil(y)
            else:
                print("_2_")
                return math.ceil(y + 0.0001)
        
        if ((max(B) == y) and (y <= 0)):
            if 1 not in B:
                print("_3_")
                return 1

        if (y < 0) and (B[x] > 0):
            if 1 not in B:
                print("_4_")
                return 1

        if (abs(B[x] - y) == 1):
            continue
        elif y <= 0:
            continue
        else:
            if (y < 1):
                print("_5_")
                return math.ceil(y)
            else:
                print("_6_")
                return math.ceil(y + 0.0001)

print(solution(array))