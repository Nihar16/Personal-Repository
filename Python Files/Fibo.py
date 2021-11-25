def fibo(n):
        a=0
        b=1
        for i in range(n):
                element=a
                a=b
                b=element+a
                print(element)
        return b
