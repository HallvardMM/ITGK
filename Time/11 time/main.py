# Hovedmodulen main

# Importerer moduler som skal brukes i main
import bruker                                   # Brukergresesnitt (bruker.py)
import fil                                      # Filbehandling (fil.py)

# Opprette variabler og initierer dem (gi dem verdier)
db = {}                                         # Oppretter en tom dictionary
dbid = 0                                        # id til dictionary som settes til 0

# Gi en varm velkomst til bruker
bruker.velkommen()                              # Skriver ut velkomst til bruker

# Viser en valgmeny til bruker
valg = bruker.valgmeny()                        # Lar bruker velge hva hun/han skal gjøre

while(valg != 7):                               # Løkke helt til 'avslutt' er valgt
  if valg == 1 or valg == 2:                    # Registrer Inntekt eller utgift
    dbid+=1                                     # Øker databaseid med en
    db = bruker.registrer(db,dbid,valg)
  elif valg == 6: 
    bruker.vis(db)                              # Viser innhold i dict. (regnskapet)
  elif valg == 5:
    bruker.fjern(db)                            # Fjerne et innslag i dict.
  elif valg == 4:
    filnavn = bruker.velgfilnavn()              # Spør bruker om filnavn
    fil.save(db,filnavn)                        # Lagrer dictionary til fil
  elif valg == 3:
    filnavn = bruker.velgfilnavn()
    db = fil.load(filnavn)                      # Laster inn dictionary fra fil
    dbid = max(db)                              # Finner største id
    bruker.melding(filnavn+' er lastet inn.')
  else:
    bruker.melding('Feil kommando')
  valg = bruker.valgmeny()
  
