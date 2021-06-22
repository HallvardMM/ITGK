#Øving 7 oppgave 8
#a
def add_data(user):
    return user.split(" ")

print(add_data("Mark Zuckerberg 32 Male Married"))
    
#b
def get_person(given_name,facebook):
    return_list=[]
    for i in range(len(facebook)):
        if facebook[i][0]==given_name:
            return_list.append(facebook[i])
    return return_list

facebook = [["Mark", "Zuckerberg", 32, "Male", "Married"],["Therese", "Johaug", 28, "Female", "Complicated"],["Mark", "Wahlberg", 45, "Male", "Married"],["Siv", "Jensen", 47, "Female", "Single"]]

print(get_person("Mark", facebook))

#c
def main():
    facebook=[]
    print("""Hello, welcome to Facebook. Add a new user by writing "given_name surname age gender relationship_status".""")
    while True: 
        s=input("Add a new user: ")
        if s=="done":
            break
        else:
            facebook.append(add_data(s))
    print("Ok")
    while True:
        x=str(input("Search for a user: "))
        if x!="done":
            print(get_person(x, facebook))
        else:
            break
main()


    
    
    
    
