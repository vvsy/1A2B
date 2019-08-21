import random

pool = []
for i in range(10):
    pool.append(i)

answer = ""
xx = []
random.choice(pool)
for times in range(3):
    a = random.choice(pool)
    pool.remove(a)
    xx.append(str(a))
    answer = answer + "%r" % a

print('start!!!')
x = input("guess:")

Ground = 1

print("round", Ground)

while answer != x:
    answerlist = xx
    Ground += 1
    A = 0
    B = 0
    for i in range(3):
        if x[i] == answer[i]:
            A += 1
        elif x[i] != answer[i]:
            if x[i] in answerlist:
                B += 1
        else:
            print("0 A 0 B")
    print(A, "A", B, "B")
    print("round", Ground)
    x = input("guess:")

print(answer)
