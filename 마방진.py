def m(n):

    A=[[0]*n for i in range(n)]

    t=1

    if n%2: 

        x, y = (n-1)//2, n-1

        for i in range(n*n):

            A[x][y]=t

            x+=1

            y+=1

            t+=1

            x%=n

            y%=n

            if A[x][y]:

                x-=1

                y-=2

 

    else: 

        x, y = 0, 0

        if N%4: 

            hn=n//2

            Q=m(hn)

            for x in range(n):

                for y in range(n):

                    if x<hn:

                        num = 3 * (not((y<hn)^(x<n//4)))

                    else:

                        num = (not((y<hn) ^ (x<n-n//4+1))) + 1

                    if y%hn==(hn-1)//2 and x<hn: A[(x+1)%hn][y] = num

                    else: A[x][y] = num

            num=hn*hn

            for x in range(n):

                for y in range(n):

                    A[x][y] *= num

                    A[x][y] += Q[x%hn][y%hn]

                        

 

        else: 

            rev_f=False

            hn=n//2

            nl=[i for i in range(n*n)]

            for x in range(n):

                if x==hn: rev_f = not rev_f

                for y in range(n):

                    rev_f = not rev_f

                    if y==hn: rev_f = not rev_f

                    if rev_f: A[x][y] = nl.pop(nl.index(x+y*n))+1

            x, y = 0, 0

            for x in range(n):

                for y in range(n):

                    if not A[y][x]: A[y][x]=nl.pop()+1

    return A

    

 

def printm(L, N):

    for i in range(N):

        for j in range(N):

            print('%5d' % L[j][i], end='')

        print("\n")

    print(checkm(L,N))

 

 

def checkm(L, N):

    c1, c2, c3, c4 = 0, 0, 0, 0

    cnum = N*(N*N+1)/2

    for x in range(N):

        for y in range(N):

            if x==y: c1+=L[x][y]

            if x+y+1==N: c2+=L[x][y]

            c3+=L[x][y]

            c4+=L[y][x]

        if c3 != cnum or c4 != cnum: return 1

        c3, c4 = 0, 0

    if c1 != cnum or c2 != cnum: return 2

    return ""

        

 

 

if __name__ == '__main__':
    while(True):

        N=int(input("마방진의 크기를 말씀해 주세요. : "))

        if N==0:
            print("마반진의 크기는 2보다 커야해요.")
        
        if N==1:
            print("마방진의 크기는 2보다 커야 한다고....")

        if N==2:
            print("하~ 마방진 크기는 2보다 크다고.....")

        else: printm(m(N), N)





