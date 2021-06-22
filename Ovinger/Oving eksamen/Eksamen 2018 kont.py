#Eksamen 2018 kont
# 1B,2b,3c (feil-a),4b,5d,6c(feil-b),7b,8c,9c,?,?,12b(feil-a),13c,14c,15a,16b,17c,18d,19d,20c(feil-a)
# 3 feil og 2 ikke gjort

#2a 68
#returner  z = (innparameter y) + (innparameter x)*2^(z-1).

#2c returnerer itgkerkult
# tar hver y. bokstav i input streng

#2e printer CALIFORNIA
# for verdier i input returnerer den en strneg med bokstaven etter A

# 2g returnerer(6,12,18,24,30,36)
# den adderer ledd på samme posisjon i hver input og returnerer en ny tuppel

#3a
def addSite(notebook):
    site=input("What is the site: ")
    username=input("Write username: ")
    password=input("Write password: ")
    if site in notebook:
        print("Site allready in notebook")
    else:
        notebook[site]=[username,[password]]
        print("Account added for",site,"\n")
    return notebook
#3b
def showSites(notebook):
    print("Nettsted:"+" "*8+"Brukernavn:"+" "*4+"Passord:")
    for keys,values in notebook.items():
        if len(keys)>15:
            print(keys[:15],+" "*(2)+values[0]+" "*(15-len(values[0]))+values[1][-1])
        else:
            print(keys,+" "*(17-len(keys)+values[0]+" "*(15-len(values[0]))+values[1][-1]))

#3c
def formatList(liste):
    streng=''
    for element in liste:
        streng+=(str(element)+", ")
    return streng
#3d
def editSite(notebook,site):
    passord=notebook[site]
    new=input("Add new site password for Facebook: ")
    if new in passord[1]:
        print("'"+new+"' has been used for",site,"already.")
        print("The following passwords have been used: ",passord[1][:-1])
        new=input("Add new site password for Facebook: ")
    passord.append(new)
    notebook[site][1]=passord
    print(site,"har been updated with a new password.")
    return notebook

#3e
def secureSites(notebook):
    passwords={}
    for keys,values in notebook.items():
        newpass=values[1][-1]
        if newpass in passwords:
            pwds[newpass].append(site)
        else:
            pwds[newpass]=[site]
    copy=False
    for newpass in passwords:
        if len(passwords[newpass])>1:
            duplicate=True
            print("You have used the password '{0}' at the following sites:{1}.".format(currentpwd,formatList(pwds[currentpwd])))
    if not copy:
        print("No sites had similar passwords. Good job!")

#4a
def importResults(file):
    fortsette='a'
    fil=False
    output=[]
    while (fil==False)and (fortsette!='q'):
        try:
            f=open(file,'r')
            if f:
                fil=True
            for line in f:
                output.append(line)
            f.close()
            return output
        except:
            fortsette=input("'"+str(file)+"' could not be found. File name ('q' exits): ")

#4b
def analyzeResults(results):
    output=[]
    for element in results:
        output.append(element.split(','))
    for element in output:
        goals=element[2].split('-')
        element=[element[0],element[1],int(goals[0]),int(goals[1])]
    return output

#4c
def calculateScores(homeGoals, awayGoals):
    if homeGoals>awayGoals:
        hjemme=3
        borte=0
    elif homeGoals<awayGoals:
        hjemme=0
        borte=3
    else:
        hjemme=1
        borte=1
    return hjemme,borte

#4d
def sumTeamValues(analyzed):
    output={}
    for element in analyzed:
        hjemme,borte=element[0],element[1]
        hjemmep,bortep=calculateScores(element[2],element[3])
        if hjemme in output:
            output[hjemme] = [output[hjemme][0] + hjemmep,output[hjemme][1] + 1]
        else:
            output[hjemme] = [hjemmep, 1]
        if borte in output:
            output[borte] = [output[borte][0] + bortep, output[borte][1] + 1]
        else:
            output[borte] = [bortep, 1]
    return output

        
#4e
def showResults(analyzed):
    print("#"*45)
    for verdier in analyzed:
        homepoints, awaypoints = calculateScores(match[2], match[3])
        if homepoints == 1:
            score = 'U'
        elif homepoints == 3:
            score = 'H'
        else:
            score = 'B'
        print("# %s%s%s - %s (%s) #"%(match[0].ljust(15), match[1].ljust(15),str(match[2]).rjust(2), str(match[3]).rjust(2),score))
    print("#"*45)

#4f
def savePoints(team_data):
    print("#" * 35)
    print("# %s %s %s #"%("Navn".ljust(15), "Poeng".ljust(6),"Kamper".ljust(6)))
    team_list = [] # Reset the list for example purposes.
    for t in team_data.items():
    # Each dictionary item: {'Name', [points, matches]}
    # Since we need to sort on points, we add t[1][0] first, then
    # name and matches
        team_list.append([t[1][0], t[0], t[1][1]])
    # team_list now looks like this: [[points, teamname, matches],[p,t,m]...]
    # Now we need to sort the list, and in the reverse order:
    # Most points (at the top)
        team_list = sorted(team_list, reverse=True)
    for team in team_list: # First name, then points and matches
        print("# %s %s %s #\n"%(team[1].ljust(15),str(team[0]).rjust(2).ljust(6), str(team[2]).ljust(6)),end="")
    print("#" * 35)  

