for _ in range(3) :
    t = int(input())
    n = 0
    for i in range(t) :
        n += int(input())
    if n == 0 :
        print('0')
    elif n > 0 :
        print('+')
    else :
        print('-')