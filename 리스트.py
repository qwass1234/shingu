a = 0
while(a != 1):
    num=int(input("리스트 크기를 입력해 :"))
    if(num == 0):
        print("종료한다.")
        break
    ma=[0]*num
    import random


    i = 0
    m = 1
    e = 1
    while(i < num):
    
        ma[i] += e
        i += 1
        e += 1
    random.shuffle(ma)
    print(ma)
    s = 0
    count = 0
    while(s < num):
        b = 0
        while(b < num-1):
            if(ma[b] > ma[b+1]):
                ma[b], ma[b+1] = ma[b+1], ma[b]
                count += 1
            b += 1  
        s += 1
    print("정렬된숫자",ma, "바뀐 횟수" ,count)
