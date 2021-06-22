#Oppgave 5
Måned=str(input("Måned: "))
Dag=int(input("Dag: "))
if (Måned=="mars" and Dag>=20) or Måned=="april" or Måned=="mai" or (Måned=="juni" and Dag<21):
    print("Vår")
elif (Måned=="juni" and Dag>=21) or Måned=="juli" or Måned=="august" or (Måned=="september" and Dag<22):
    print("Sommer")
elif (Måned=="september" and Dag>=22) or Måned=="oktober" or Måned=="november" or (Måned=="desember" and Dag<int(21)):
    print("Høst")
else:
    print("vinter") #Hvis man setter inn noe feil svarer den vinter
    
    
