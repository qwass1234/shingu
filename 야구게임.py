

n="YES"
while(n == "YES"):
    import random
    r = ["0","0","0"]
    r[0] = str(random.randrange(1,9, 1))
    r[1] = r[0]
    r[2] = r[0]
    while(r[0] == r[1]):
        r[1] = str(random.randrange(1,9,1))
    while(r[0] == r[2] or r[1] == r[2]):
        r[2] = str(random.randrange(1,9,1))

    t = 0
    s = 0
    b = 0


    print("야구게임 시작합니다.")
    print("게임도중 나가고 싶으면 0을 눌러주세요.")
    while (s < 3):

        num = str(input("숫자 3자리를 입력하세요 : "))

        s = 0
        b = 0
        x = len(num) 
        y = num.isdigit()
    
        if(num == '0'):
            print ("종료 됩니다.")
            break
        elif(x != 3):
            print ("잘못된 입력 입니다. 숫자 세개를 입력 해주세요.")
            continue
        elif(y == False):
            print ("잘못된 입력 입니다. 정수를 입력해 주세요.")
            continue
    
        for i in range(0,3):
            for j in range(0,3):
                if(num[i] == str(r[j]) and i == j):
                    s += 1
                elif(num[i] == str(r[j]) and i != j):
                    b += 1
        
        print ("결과 : [", s, "] Strike [", b, "] Ball")
        print(r)
        t += 1
    if(num == "0"):
        break
    
    print(t, "번 입력 했어요.")
    print("")
    print("한번더 하시겠습니까? yes/no?")
    n = input()
    n = n.upper()
    if(n == "YES"):
        print("다시시작")
    elif(n == "NO"):
        print("종료합니다")
        break
    elif(n != "NO"):
        while(n != "NO" or n != "YES"):
            print("다시입력해주세요")
            n = input()
            n = n.upper()
            if(n == "NO" or n == "YES"):
                break
        if(n == "NO"):
            print("종료합니다")
            break
        a -= 1
        if(ma[a][d] == 0):
            ma[a][d] += c

