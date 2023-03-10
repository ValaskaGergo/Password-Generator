import secrets
import string
import random
import time
import sys


def main():
    
    Randomvalue = welcome()

    passw = shuffle(Randomvalue)
    
    printLoading(passw)     

def welcome():
    print("\n♦   Welcome to PSW _GEN 1.23 ,")
    x = 1
    while  x < 4:
        x = int(input("\n♦   Give me a random number!  { 4 - 14 }    --->    "))

    return x

def shuffle(x):
    minUpper = random.randint(2, x)
    minLower = random.randint(2, x)
    minDigits = random.randint(1, x)
    minSpec = random.randint(0, x)
    password = ""

    for i in range(minUpper):
        password += "".join(random.choice(secrets.choice(string.ascii_uppercase)))

    for i in range(minLower):
        password += "".join(random.choice(secrets.choice(string.ascii_lowercase)))

    for i in range(minDigits):
        password += "".join(random.choice(secrets.choice(string.digits)))

    for i in range(minSpec):
        password += "".join(random.choice(secrets.choice(string.punctuation)))

    password = list(password)
    random.shuffle(password)
    
    return password

def printLoading(passwordCharacters):
    print("\n♦   Security is the key...\n")
    time.sleep(0.0812314)

    
    animation = ["        [□□□□□□□□□□]","        [□□□□□□□□□□]",
                    "        [■□□□□□□□□□]", "        [■■□□□□□□□□]",
                         "        [■■■□□□□□□□]", "        [■■■■□□□□□□]",
                             "        [■■■■■□□□□□]", "        [■■■■■■□□□□]", 
                               "        [■■■■■■■□□□]","        [■■■■■■■□□□]",
                                  "        [■■■■■■■□□□]", "        [■■■■■■■■□□]", 
                                     "        [■■■■■■■■■□]", "        [■■■■■■■■■■]"]

    for i in range(len(animation)):
        time.sleep(0.0631423)
        sys.stdout.write("\r"+ "♦   Loading..."+ animation[i % len(animation)])
        sys.stdout.flush()

    print("\n")
    print("♦   Your New PassWord : \n")
    print("♦   "+"".join(passwordCharacters)+ "\n")

main()