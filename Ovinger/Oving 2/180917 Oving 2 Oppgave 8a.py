print("INFO\nDette programmet besvarer om din utleie av egen bolig er skattepliktig.\nFørst trenger vi å vite hvor stor del av boligen du har leid ut.\nAngi dette i prosent, 100 betyr hele boligen, 50 betyr halve,\n20 en mindre del av boligen som f.eks. en hybel.")
print("----------------------------------------------------------------------\nDATAINNHENTING:")      
bolig=int(input("Oppgi hvor mye av boligen som ble utleid: "))
inntekt=int(input("Skriv inn hva du har hatt i leieinntekt: "))
  
print("----------------------------------------------------------------------\nSKATTEBEREGNING:")
if bolig>50 and inntekt>20000:
    print("Inntekten er skattepliktig")
    print("Skattepliktig beløp er "+str(inntekt))
