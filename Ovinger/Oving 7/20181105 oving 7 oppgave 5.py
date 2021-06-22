#Øving 7 oppgave 5
#a
def check_equal(str1, str2):
    if len(str1)==len(str2):
        for i in range(0,len(str1)):
            if str1[i]!=str2[i]:
                return False
        return True
    else:
        return False


str1 = 'hei'
str2 = 'hello'
str3 = 'hello'
print(check_equal(str1, str2))
print(check_equal(str3, str2))

#b
def reversed_word(string):
    return string[::-1]

def reverse_word_slower(string):
    newstring = ''
    ch = len(string)
    while ch:
        ch -= 1                    # ch = ch - 1
        newstring += string[ch] # new_string = new_string + character
    return newstring


string = 'star desserts'
print(reversed_word(string))

#c
def check_palindrome(string):
    newstring=reversed_word(string)
    if newstring==string:
        return True
    else:
        return False

str1 = 'agnes i senga'
str2 = 'hello'
print(check_palindrome(str1))
print(check_palindrome(str2))

#d
def contains_string(str1,str2):
    return str1.find(str2)
    
str1 = 'pepperkake'
str2 = 'per'
str3 = 'ola'
print(contains_string(str1, str2))
print(contains_string(str1, str3))
            
        
    
        
        
            
        
