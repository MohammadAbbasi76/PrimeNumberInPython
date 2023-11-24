while True:
    Number = int(input())  # Read a number from the input
    if Number == 2 or Number == 3:
        print('prime')  # If the number is 2 or 3, it is prime
        continue
    if Number == 1 or Number == 0:
        print('not prime')  # If the number is 1 or 0, it is not prime
        continue
    while True:
        if Number % 2 == 0:
            # If the number is divisible by 2, it is not prime
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
                    Counter = Counter + 1
                    if Counter == (Number - 1):
                        break
            if NotPrimeFlag == 0:
                # If the number has no divisors other than 1 and itself, it is prime
                print('prime')
                break
            else:
                # If the number has a divisor other than 1 and itself, it is not prime
                print('not prime')
                break
