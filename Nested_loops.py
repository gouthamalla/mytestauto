num = 100
for i in range(2, num):
    count = 0
    for j in range(2, i):
        if i%j == 0:
            count += 1
    if count ==0:
        print('num', i, ' is prime')