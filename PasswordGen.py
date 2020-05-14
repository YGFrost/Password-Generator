import random
import time

results = []

def script():

 global length
 try:
  length = int(input("Please type the length: "))

 except ValueError:
     print("Error [1], Please try again")
     script()

script()

def reset():
 global ynum
 ynum = input("Do you want numbers Y/N")

 if ynum == "N" or ynum =="n":
     peep = 0
     while peep != length:
         peep += 1
         global word
         word = random.choice("AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz")
         print(word, end="")

 elif ynum == "Y" or ynum == "y":
     word = random.choice("AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz")
     print("Geting password ready...")
     time.sleep(0.7)
     peep = 0
     while peep != length:
         peep += 1
         num = random.choice("1234567890")
         word = random.choice("AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz")
         password = random.choice([num,word])
         results.append(password)
         print(*results,sep="")
 else:
     print("Please try again..")
     reset()
reset()
saving = input("Great now do you want to save.. ?")

if saving == "Y" or saving == "y":
    folder = open('Passwords.txt', "w")
    folder.write("".join(results))
    print("Done King :]")
else:
  print("Umm byeee XD")