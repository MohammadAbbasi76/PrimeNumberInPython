
while True:
    Number = int(input())
    if Number==2 or Number==3 :
        print('prime')
        continue
    if Number ==1 or Number==0:
        print('not prime')
        continue
    while True:
        if Number % 2 == 0:
            print('not prime')
            break
        else:
            Counter = 2
            NotPrimeFlag = 0
            while True:
                if Counter < Number:
                    Temp = Number % Counter
                    if Temp == 0:
                        NotPrimeFlag = 1
                    Counter = Counter+1
                    if Counter == (Number-1):
                        break
            if NotPrimeFlag == 0:
                print('prime')
                break
            else:
                print('not prime')
                break
