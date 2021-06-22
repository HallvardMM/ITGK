# Modulen bruker (bruker.py) som blir importert av main.py



#Skriver ut velkomsthilsen til skjerm
def velkommen():
  print('Velkommen til Hybelregnskapsprogram v 3.0')
  print('=========================================')




#Skriver ut meny til skjerm og returnerer brukerens menyvalg
def valgmeny():
  print('\nVelg kommando (1-7):')
  print('1: Registrer inntekt')
  print('2: Registrer utgift')
  print('3: Last inn regnskap')
  print('4: Lagre regnskap')
  print('5: Fjern et innslag')
  print('6: Vis regnskapet')
  print('7: Avslutt')
  
  valg = int(input('\nKommando: '))
  return valg



# Registrer postering (inntekt eller utgift) i regnskap 
def registrer(db,dbid,valg): 
  if valg == 1:
    print('Registrering av inntekt')
  else:
    print('Registrering av utgift')
          
  dato = input('Dato [yyyy-mm-dd]: ')
  belop = float(input('Belop [kr]: '))
  beskrivelse = input('Beskrivelse [tekst]: ')
  
  if valg == 2:                                 # Registreringen er en utgift
    belop = belop *-1                           # Ganger med -1 for utgift

  db[dbid] = [dato,belop,beskrivelse]           # Legger inn postering i dict.

  melding('Data er registrert')                 # Skriver ut bekrevtelse til skjerm
  return db                                     # Returnerer databasen (dict.)



# Skriv melding til skjerm
def melding(tekst): 
  print('>>>',tekst)



# Viser hele regnskapet (alt i dict.)
def vis(db): 
  balanse = 0                                   # Brukes til beregning av balanse

  #Overskrift
  header = '\nID'.rjust(4)+' Dato'.ljust(11)+' '+'Beskrivelse'.ljust(30)+'Sum'
  print(header)
  print('=======================================================')

  for x in db:                                  # Går igjennom nøklene i dict.
    liste = db[x]                               # Henter ut verdien knyttet til elementet med nøkkelen x.
                                                    # dvs. listen [dato,belop,beskrivelse]
    s=str(x).rjust(2)+liste[0].rjust(11)        # ID og dato
    s+=' '+liste[2].ljust(30)                   # Beskrivelse venstrejustert 30 tegn
    s+=str(liste[1]).rjust(5)                   # Beløp høyerejustert 5 tegn
    print(s)
    
    balanse+=liste[1]                           # Oppdatarer balanse 
  print('\nBalanse:',balanse)



#Fjerner post i regnskap
def fjern(db):
  print('IDer i databasen: ',db.keys())
  dbid = int(input('ID på innslag som skal fjernes: '))
  if (dbid in db):                              # Sjekker om dbid finnes i db
    del db[dbid]                                # Fjerne post fra dictionary
    melding('Innslag med ID '+str(dbid)+' er fjernet')
  else:
    melding('ID '+str(dbid)+' finnes ikke i databasen')
  return db                                     # Returner dictionarien



#Ber bruker taste inn filnavn
def velgfilnavn():
  filnavn = input('Velg filnavn: ')
  return filnavn
