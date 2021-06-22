# Modul fil - filfunksjoner (brukt av main)
import pickle             # Bibliotek som muliggjør lagring/lasting av dict. til/fra disk

# Lagrer dict. til fil
def save(db,filnavn): 
  f = open(filnavn,'bw')  # Åpner fil for skriving binært (ikke tekst)
  pickle.dump(db,f)       # Dumper innhold i dict. til binærfil
  f.close()

# Laster dict. fra fil
def load(filnavn):
  f = open(filnavn,'br')  # Lesing bineart
  db = pickle.load(f)     # Laster inn dict. fra fil
  f.close()
  return db
  
