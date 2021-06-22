#Øving 2 oppgave 4c)

prom = float(input("Hvor stor var promillen? "))
if prom > 0.5:
    print("Bot: en halv brutto månedslønn, samt fengsel.")
elif prom > 0.4:
    print("Forelegg: 10000,-")
elif prom > 0.2:
    print("Forelegg: 6000,-")
elif prom < 0.2:
    print("Ikke straffbart, ingen bot.")
