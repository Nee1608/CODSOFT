import random

def pass_gen(lenght):
    
    list_of_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_"
    
    #creating a empty password string
    password = " "

    #loop that will go upto the lenght of password
    for i in range(lenght):
        #random.choice() function is used to select random character from the list_of_chars and concatenate it with passwd string
        password = password + random.choice(list_of_chars)

    return password


print("Enter the lenght of password to be generated:  ")
lenght = int(input())

password = pass_gen(lenght)
print("Random generated password is:  ",password)