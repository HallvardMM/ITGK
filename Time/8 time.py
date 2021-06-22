#Filer og unntak

#f=open('filnavn',w,encoding='utf-8') Åpner fil for skriving
filnavn=input("filnavn ")
f=open(filnavn,"r")

for line in f:
    tall=f.readline(line)
    
