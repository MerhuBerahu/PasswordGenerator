#!/usr/bin/env python

"""
=====================================
Password Generator
=====================================
Usage: %prog
:Author: MerhuBerahu, https://github.com/MerhuBerahu
:Date: 22/08/2020
"""
import random
import tkinter

# ask for complexity
    #to be implemented maybe

# Password Generation
def generate(*args):
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special = """{}[]()/\'"`~,;:.<>@#$£%^&*"""
    number = "1234567890"
    password = ""
    password_pool = []
    character_pool = []    

    if check_special.get() == True:
        character_pool.append(special)
    if check_Lower.get() == True:
        character_pool.append(lower)
    if check_Upper.get() == True:
        character_pool.append(upper)
    if check_Numbers.get() == True:
        character_pool.append(number)
    #character_pool = ''.join(character_pool)


    print(f"args: {args}")
    print(f"character_pool: {character_pool}")
    print(f"number: {number}")
    print(f"check_Numbers.get(): {check_Numbers.get()}")

    # Issue with below is you may get a random pw but it might randomly not 
    # pick any numbers even if you had the checkbox ticked 
    # To get around this we need to keep seperate list indexes, divide the 
    # pw_length by number of indexes in character_pool, then get a random
    # sample for each index, join those and randomize to get final Password

    #password = "".join(random.sample(character_pool,pw_length.get())) # not guarenteed to include all characters
    num = pw_length.get() // len(character_pool)
    for i in character_pool:
        selection = random.sample(i,num)
        password_pool.append(selection)

    # TESTING
    print(f"Password Pool: {password_pool}")
    #password_pool = ''.join(random.shuffle(password_pool)) # TypeError: can only join an iterable ???
    for i in password_pool:
        print(i, type)
    print(f"Character Pool: {character_pool}")
    print(f"Selection: {selection}")
    print(f"Password Pool: {password_pool}")
    print(password)


# create GUI
window = tkinter.Tk()
window.title("Password Generator")
 
# Determine password length
pw_length = tkinter.IntVar()
tkinter.Label(window, text = "Password Length:").grid(row = 0, column = 0, sticky="W") 
check__pw_length = tkinter.Spinbox(window, from_=8, to_=50, textvariable=pw_length, width=13).grid(row = 0, column = 1, sticky="W")

# 'Checkbutton' class is for creating a checkbutton which will take a 'columnspan' of width two (covers two columns)
check_special = tkinter.BooleanVar()
check_special.set(True)
tkinter.Label(window, text = "Include Special Characters:").grid(row = 1, column = 0, sticky="W") 
tkinter.Checkbutton(window, text = "( e.g. @#$% )", var=check_special).grid(row = 1, column = 1, sticky="W")  

check_Numbers = tkinter.BooleanVar()
check_Numbers.set(True)
tkinter.Label(window, text = "Include Numbers:").grid(row = 2, column = 0, sticky="W") 
tkinter.Checkbutton(window, text = "( e.g. 123456 )", var=check_Numbers).grid(row = 2, column = 1, sticky="W")  

check_Lower = tkinter.BooleanVar()
check_Lower.set(True)
tkinter.Label(window, text = "Include Lowercase Characters:").grid(row = 3, column = 0, sticky="W") 
tkinter.Checkbutton(window, text = "( e.g. abcdefgh )", var=check_Lower).grid(row = 3, column = 1, sticky="W")  

check_Upper = tkinter.BooleanVar()
check_Upper.set(True)
tkinter.Label(window, text = "Include Uppercase Characters:").grid(row = 4, column = 0, sticky="W") 
tkinter.Checkbutton(window, text = "( e.g. ABCDEFGH )", var = check_Upper).grid(row = 4, column = 1, sticky="W")  

check_Similar = tkinter.BooleanVar()
check_Similar.set(False)
tkinter.Label(window, text = "Exclude Similar Characters:").grid(row = 5, column = 0, sticky="W") 
tkinter.Checkbutton(window, text = "( e.g. i, l, 1, L, o, 0, O )", var=check_Similar).grid(row = 5, column = 1, sticky="W")  

check_Ambiguous = tkinter.BooleanVar()
check_Ambiguous.set(False)
tkinter.Label(window, text = "Exclude Ambiguous Characters:").grid(row = 6, column = 0, sticky="W") 
tkinter.Checkbutton(window, text = "( { } [ ] ( ) / \\ ' \" ` ~ , ; : . < > )", var=check_Ambiguous).grid(row = 6, column = 1, sticky="W")  

button_widget = tkinter.Button(window,text="GENERATE", command=lambda:generate(check_special.get(), check_Numbers.get(), check_Lower.get(),check_Upper.get(),pw_length.get())).grid(row = 9, column = 0) 



window.mainloop()


