import random
print("\033[1;33m")  # Yellow color start

print("""
__| |______________________________________________________________________________| |__
__   ______________________________________________________________________________   __
  | |                                                                              | |  
  | |                                                                              | |  
  | |                                                                              | |  
  | |     _          _   _                                       _                 | |  
  | |    | |        | | ( )                                     | |                | |  
  | |    | |     ___| |_|/ ___    __ _  ___ _ __   ___ _ __ __ _| |_ ___    __ _   | |  
  | |    | |    / _ \ __| / __|  / _` |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \  / _` |  | |  
  | |    | |___|  __/ |_  \__ \ | (_| |  __/ | | |  __/ | | (_| | ||  __/ | (_| |  | |  
  | |    |______\___|\__| |___/  \__, |\___|_| |_|\___|_| _\__,_|\__\___| _\__,_|  | |  
  | |                             __/ |          | | | | | |         | | ( )       | |  
  | |   _ __   __ _ ___ _____    |___/__  _ __ __| | | |_| |__   __ _| |_|/ ___    | |  
  | |  | '_ \ / _` / __/ __\ \ /\ / / _ \| '__/ _` | | __| '_ \ / _` | __| / __|   | |  
  | |  | |_) | (_| \__ \__ \\ V  V / (_) | | | (_| | | |_| | | | (_| | |_  \__ \   | |  
  | |  | .__/ \__,_|___/___/ \_/\_/ \___/|_|  \__,_|  \__|_| |_|\__,_|\__| |___/   | |  
  | |  | |                                                                         | |  
  | |  |_|                   _       _                              _    _         | |  
  | |  | |                  | |     | |                            | |  | |        | |  
  | |  | |_ ___  _   _  __ _| |__   | |_ ___     ___ _ __ __ _  ___| | _| |        | |  
  | |  | __/ _ \| | | |/ _` | '_ \  | __/ _ \   / __| '__/ _` |/ __| |/ / |        | |  
  | |  | || (_) | |_| | (_| | | | | | || (_) | | (__| | | (_| | (__|   <|_|        | |  
  | |   \__\___/ \__,_|\__, |_| |_|  \__\___/   \___|_|  \__,_|\___|_|\_(_)        | |  
  | |                   __/ |                                                      | |  
  | |                  |___/                                                       | |  
  | |                                                                              | |  
  | |                                                                              | |  
__| |______________________________________________________________________________| |__
__   ______________________________________________________________________________   __
  | |                                                                              | |  
""")

print("\033[0m")  # Reset color

s="🔐 Welcome to the password generator!"
print("\033[1;3;35;47m" + s.center(100) + "\033[0m")

print("\nChoose password difficulty level.\n")
print("Enter what type of level you want to make your password: ")
print("\033[1;32m 1) Easy\033[0m")
print("\033[1;33m 2) Medium\033[0m")
print("\033[1;31m 3) Hard\033[0m\n")

level=int(input("Enter your choice: (1/2/3) \n"))

if level not in [1,2,3] :
    print("\n\033[1;31m ⚠️  Error : Invalid choice! Please run again and enter 1 , 2 or 3.\033[0m")
   
else :
    tletters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    tdigits = "0123456789"
    tsymbols = "[!@#$%^&*()_+-=|<>?/,.:;]"

    password=[]

    if level==1:
      length = int(input("\nEnter the length of the password:"))
      for i in range(length):
         password.append(random.choice(tletters))

    elif level==2:
      length = int(input("\nEnter the length of the password:"))
      letters = int(input("\nHow many letters (a-z, A-Z) you want to add in your password: "))
      digits = int(input("\n How many digits (0-9) you want: "))

      if (letters+digits!=length):
        print("\n\033[1;31m ⚠️  Error : Letters and digits must equal to length!\033[0m")
        exit()
      else:
        for i in range(letters):
                password.append(random.choice(tletters))
        for i in range(digits):
                password.append(random.choice(tdigits))

    elif level==3:
      length = int(input("\nEnter the length of the password:"))
      letters = int(input("\nHow many letters (a-z, A-Z) you want to add in your password: "))
      digits = int(input("\n How many digits (0-9) you want: "))
      symbols = int(input("\nHow many special characters (!@#$...) you want: "))

      if (letters+digits+symbols!=length):
        print("\n\033[1;31m ⚠️  Error : Letters, digits and special symbols must equal to length!\033[0m")
        exit()
      else:
          for i in range(letters):
                password.append(random.choice(tletters))
          for i in range(digits):
                password.append(random.choice(tdigits))
          for i in range(symbols):
                password.append(random.choice(tsymbols))

random.shuffle(password)
final = " ".join(password)
print("\n\033[1;32m ✅ Your Password is generated: 👏 \033[0m")
print("\n\033[1;30;47m " + final + " \033[0m")
print("\n\033[1;30;103m Thanks for using 😄 \033[0m")
