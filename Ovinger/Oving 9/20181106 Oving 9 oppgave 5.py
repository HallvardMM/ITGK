#øving 9 oppgave 5
cheeses = {
'cheddar':
('A235-4', 'A236-1', 'A236-2', 'A236-3', 'A236-5', 'C31-1', 'C31-2'),
'mozarella':
('Q456-9', 'Q456-8', 'A234-5', 'Q457-1', 'Q457-2'),
'gombost':
('ZLAFS55-4', 'ZLAFS55-9', 'GOMBOS-7', 'A236-4'),
'geitost':
('SPAZ-1', 'SPAZ-3', 'EMACS45-0'),
'port salut':
('B15-1', 'B15-2', 'B15-3', 'B15-4', 'B16-1', 'B16-2', 'B16-4'),
'camembert':
('A243-1', 'A234-2', 'A234-3', 'A234-4', 'A235-1', 'A235-2', 'A235-3'),
'ridder':
('GOMBOS-4', 'B16-3'),
}

#a
print(cheeses['port salut'])

#b

infected_slots=['B13','B14','B15','A234','A235','C31']
infected_cheese=[]
print(cheeses.values())


for key in cheeses:
    for j in cheeses[key]:
        for k in infected_slots:
            if j.find(k) != -1:
                if key not in infected_cheese:
                    infected_cheese.append(key)

#issubstring()
            
print("Potentially infected cheeses:",infected_cheese)


#c
not_infected_cheese=[]
for key in cheeses:
    if key not in infected_cheese:
        not_infected_cheese.append(key)

for key,value in cheeses.items():
    if key in not_infected_cheese:
            for i in range(len(value)):
                print(value[i]," "*(9-(len(value[i]))),key) 
         
        
