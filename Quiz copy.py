import time, sys,random
top="""                       \x1b[34m▄     █ ▄▀  ▄
                   ▄   ▀▄▄▄▀█▀▀█▀▀▄█▄ █
                    ▀▄▄▀█\x1b[33m░░░\x1b[34m▀\x1b[33m░░░░░░░░\x1b[34m█▄ ▄▀▀
                ▀▀▄ █▀\x1b[33m░░░░░░░░░\x1b[34m▄▄▄▄▄▄\x1b[33m░\x1b[34m▀█
                 ▄▀▀\x1b[33m░\x1b[34m▄▄▀▀▀▄\x1b[33m░░\x1b[34m▄█▀    ▀▄\x1b[33m░\x1b[34m▄█▀▀▀▄
              ▄▄██\x1b[33m░░\x1b[34m█      █\x1b[33m░\x1b[34m█  \x1b[33m███ \x1b[34m▄▀\x1b[33m░░░\x1b[34m██\x1b[33m░\x1b[34m█
             █\x1b[33m░\x1b[34m▄█\x1b[33m░░░\x1b[34m█ \x1b[33m███ \x1b[34m▄▀\x1b[33m░\x1b[34m▀▀▄███▀\x1b[33m░░░░░\x1b[34m██\x1b[33m░\x1b[34m█
     \x1b[34m        █\x1b[33m░\x1b[34m▀█▄\x1b[33m░░\x1b[34m▀▄███▄▀\x1b[33m░░░░░░░░░░░░░\x1b[34m▄█▄▀
       \x1b[34m       ▀▀▀▀█\x1b[33m░░░░░░░░░░░░░░░\x1b[34m▄█▀\x1b[33m░░\x1b[34m▄▀    ▄
          \x1b[34m     ▄   ▀▄\x1b[33m░\x1b[34m▀▀▄▄\x1b[33m░░░░░\x1b[34m▄▄▀▀ \x1b[33m░\x1b[34m▄▀    ▄█▀
          \x1b[34m   ▄▄█▄    ▀▀▄▄\x1b[33m░\x1b[34m▀▀▀▀▀\x1b[33m░\x1b[34m▄▄▄▀▀  ▄▄▀▀▀█▀▀
          \x1b[34m   ▄█▀▀▀▀▄▄▄▄  ▀▀▀▀▀█▀   ▄▄▀▀      ▀
          \x1b[34m             ▀▀▀▀▀▄▄█▄▄▀▀
                             ░░░
                              ░"""

bot="""\x1b[33m░██████╗░██╗░░░██╗██╗███████╗\x1b[34m░░░\x1b[33m██████╗░░█████╗░███╗░░░███╗███████╗
██╔═══██╗██║░░░██║██║╚════██║ \x1b[34m░\x1b[33m██╔════╝░██╔══██╗████╗░████║██╔════╝
██║██╗██║██║░░░██║██║░░███╔═╝  ██║░░██╗░███████║██╔████╔██║█████╗░░
╚██████╔╝██║░░░██║██║██╔══╝░░  ██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░
░╚═██╔═╝░╚██████╔╝██║███████╗  ╚██████╔╝██║░░██║██║░╚═╝░██║███████╗
░░░╚═╝░░░░╚═════╝░╚═╝╚══════╝  ░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝"""

mid="""\x1b[33m░░░╚═╝░░░░╚═════╝░╚═╝╚══════╝  ░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚\x1b[36m🆃 🅸 🅼 🅴 ❗❗❗"""

side="""\x1b[33m╔══╦╗
╚╣╠╝╚╦╗
 ║╠╗╔╣╠══╗
 ║║║║╚╣══╣
╔╣╠╣╚╗╠══║
╚══╩═╝╚══╝"""

hello="""ℍ 𝕖 𝕝 𝕝 𝕠 
𝕋 𝕙 𝕖 𝕣 𝕖...

"""

    
print(top)
time.sleep(1)
sys.stdout.write("\033[12F")
print(hello)
time.sleep(2)
print(side)
time.sleep(1)
print(bot)
time.sleep(1.5)
sys.stdout.write("\033[F")
print(mid)
time.sleep(2)
sys.stdout.write("\033[F")
print("\n\n\x1b[34mARE YOU READY TO PLAY IN                     ")
time.sleep(1.5)
sys.stdout.write("\033[F")
print("\x1b[34mARE YOU READY TO PLAY IN \x1b[31m𝕋 ℍ ℝ 𝔼 𝔼")
time.sleep(1.5)
sys.stdout.write("\033[F")
print("\x1b[34mARE YOU READY TO PLAY IN \x1b[33m𝕋 𝕎  𝕆    ")
time.sleep(1.5)
sys.stdout.write("\033[F")
print("\x1b[34mARE YOU READY TO PLAY IN \x1b[32m𝕆 ℕ 𝔼     ")
time.sleep(1)
sys.stdout.write("\033[F")
print("\x1b[32m𝕊 𝕋 𝔸 ℝ 𝕋 ❕                                 ")
n=0
score=0
def q1():
    global score,n
    n+=1
    answer=input(f"\n\x1b[35mQuestion {n}: \x1b[34mIt is the function that prints the specified message to the screen, or other standard output device.\x1b[30m ").lower()
    if answer=='print function' or answer=='print':
        score += 1
        print('\x1b[32mcorrect')
    else:
        print('\x1b[31mWrong Answer :(')

def q2():
    global score,n
    n+=1
    answer=input(f'\n\x1b[35mQuestion {n}: \x1b[34mIt is a type of function that allows user input.\x1b[30m ').lower()
    if answer=='input function' or answer=='input':
        score += 1
        print('\x1b[32mcorrect')
    else:
        print('\x1b[31mWrong Answer :(')

def q3():
    global score,n
    n+=1
    answer=input(f'\n\x1b[35mQuestion {n}: \x1b[34mIt is a function that determines the data type of a value in Python.\x1b[30m ').lower()
    if answer=='type function' or answer=='type':
        score += 1
        print('\x1b[32mcorrect')
    else:
        print('\x1b[31mWrong Answer :(')

def q4():
    global score,n
    n+=1
    answer=input(f'\n\x1b[35mQuestion {n}: \x1b[34mWhat operand type is supported in "string and sting" and in "string and integer" in Python?\x1b[30m ').lower()
    if answer=='+ and *' or answer=='+*':
        score += 1
        print('\x1b[32mcorrect')
    else:
        print('\x1b[31mWrong Answer :(')

def q5():
    global score,n
    n+=1
    answer=input(f'\n\x1b[35mQuestion {n}: \x1b[34mWhat encloses a list in Python?\x1b[30m ').lower()
    if answer=='bracket' or answer=='[]':
        score += 1
        print('\x1b[32mcorrect')
    else:
        print('\x1b[31mWrong Answer :(')

def q6():
    global score,n
    n+=1
    answer=input(f'\n\x1b[35mQuestion {n}: \x1b[34mWhat encloses a tuple in Python?\x1b[30m ').lower()
    if answer=='parenthesis' or answer=='()':
        score += 1
        print('\x1b[32mcorrect')
    else:
        print('\x1b[31mWrong Answer :(')

def q7():
    global score,n
    n+=1
    answer=input(f'\n\x1b[35mQuestion {n}: \x1b[34mTrue or False: It is possible to assign multiline string to a variable in Python.\x1b[30m ').lower()
    if answer=='true' or answer=='t':
        score += 1
        print('\x1b[32mcorrect')
    else:
        print('\x1b[31mWrong Answer :(')

def q8():
    global score,n
    n+=1
    answer=input(f"\n\x1b[35mQuestion {n}: \x1b[34mTrue or False: A string can change it's value unlike tuple which is immutable by nature in Python.\x1b[30m ").lower()
    if answer=='false' or answer=='f':
        score += 1
        print('\x1b[32mcorrect')
    else:
        print('\x1b[31mWrong Answer :(')

def q9():
    global score,n
    n+=1
    answer=input(f'\n\x1b[35mQuestion {n}: \x1b[34mIt is the statement that is used for decision-making and execute both the true part and the false part of a given condition in Python.\x1b[30m ').lower()
    if answer=='if/else':
        score += 1
        print('\x1b[32mcorrect')
    else:
        print('\x1b[31mWrong Answer :(')

def q10():
    global score,n
    n+=1
    answer=input(f'\n\x1b[35mQuestion {n}: \x1b[34mIt is a chunk of codes that you can use repeatedly rather than writing it down multiple times and only runs when called.\x1b[30m ').lower()
    if answer=='function':
        score += 1
        print('\x1b[32mcorrect')
    else:
        print('\x1b[31mWrong Answer :(')

questions=[1,2,3,4,5,6,7,8,9,10] 

time.sleep(2)
while questions != []:
    x = random.choice(questions)
    index = questions.index(x)
    questions.pop(index)
    questions=questions

    if x==1:
        q1()
    elif x==2:
        q2()
    elif x==3:
        q3() 
    elif x==4:
        q4()
    elif x==5:
        q5()
    elif x==6:
        q6()
    elif x==7:
        q7()
    elif x==8:
        q8()
    elif x==9:
        q9()
    elif x==10:
        q10()
c = 7
d="\x1b[33mcalculating"
print(" ")
print(d)
while c != 0:
    time.sleep(.5)
    sys.stdout.write("\033[F")
    print(d)
    d += "."
    c-=1
time.sleep(1)
sys.stdout.write("\033[F")
print("\x1b[30mThankyou for Playing this small quiz game, you've answered\x1b[33m",score,"\x1b[30mquestions correctly!") 
print('\x1b[33mBYE!\n\x1b[30m')