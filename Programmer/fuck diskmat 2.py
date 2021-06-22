while True:
    Del=int(input("Hvilken del av oppgave 4.6 26 ønsker du? 1/2 "))
    
    if Del==1:
        for x in range(1, 3120+1):
            if 17*x%3120==1:
                print(x)

    elif Del==2:

        C=int(input("C = "))
        d=int(input("d = "))
        mod=int(input("mod = "))

        print(C**d%mod)
