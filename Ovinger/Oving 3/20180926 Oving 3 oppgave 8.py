#Øving 4 oppgave 8a

while True:
    oppgave=str(input("Hvilken oppgave ønsker du (a/b): "))
    if oppgave=="a":
        k=int(input("Hvilken k ønsker du? "))
        def F(k):
            if k == 0: return 0
            elif k == 1: return 1
            else: return F(k-1)+F(k-2)
        print(F(k))
    #Dette er en bedre kode return ((1+(5**0.5))**k-(1-(5**0.5)))**k)/(2**k*(5**0.5))

    #øving 4 oppgave 8b
    if oppgave=="b":
        k=int(input("Hvilken k ønsker du? "))


        def SumF(k) : 
            if k ==0: return 0
           
            fibonaci =[0] * (k+1) 
            fibonaci[1] = 1
           
            summen = fibonaci[0] + fibonaci[1] 
           
            for i in range(2,k+1) : 
                fibonaci[i] = fibonaci[i-1] + fibonaci[i-2] 
                summen = summen + fibonaci[i] 
                  
            return summen
  
  
        print("Sumen av Fibonacci tallene er : " , 
              SumF(k)) 
          
