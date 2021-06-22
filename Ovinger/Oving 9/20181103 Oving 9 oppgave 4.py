#øving 9 oppgave 4
#a
def write_to_file(data):
    f = open('my_file.txt', 'a') #a for append ikke w for write. Da det overskriver.
    f.write(data)
    f.close()

#b
def read_from_file(filename):
    f = open(filename, 'r')
    innhold = f.read()
    print(innhold)
    f.close()

#c
def main():
    y=True
    while y:
        q=input("Do you want to read or write? ")
        if q=="write":
            q1=input("What do you want to write to file? ")
            write_to_file(q1)
            print(q1, "was written to file.")
        elif q=="read":
            read_from_file('my_file.txt')
        elif q=="done":
            y=False

main()
