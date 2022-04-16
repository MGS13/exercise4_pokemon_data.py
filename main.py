import time, os

print('''
___  ___           _    ___________                _       
|  \/  |          | |  |  ___| ___ \              | |      
| .  . | ___   ___| | _| |__ | |_/ / ___  __ _ ___| |_ ___ 
| |\/| |/ _ \ / __| |/ /  __|| ___ \/ _ \/ _` / __| __/ __|
| |  | | (_) | (__|   <| |___| |_/ /  __/ (_| \__ \ |_\__ \
\_|  |_/\___/ \___|_|\_\____/\____/ \___|\__,_|___/\__|___/

            OFFICIAL MOCKÉBEASTS MOCKÉDEX
''')
time.sleep(2)
os.system('clear')
#while(True):
 # pass #your code starts here
class mockbeast:
  name = " "
  type = " "
  smov = " "
  HP = 1
  MP = 1
  def __init__(self):
    print("New Mockbeast created")

leaderboard = []
try:
  f = open("text.txt", "r")
  leaderboard = eval(f.readline())
  f.close()
except:
  pass

while(True):
  print("== MockeDex ==\n")
  name = input("Name: ")
  type = input("Type: ")
  types=["earth", "wind", "fire", "spirit"]
  while (type not in types):
    print("That is not a type!\n There are earth, wind, fire, and spirit")
    type = input("Type: ")
  smove = input("Special Move: ")
  HP = int(input("HP: "))
  while (HP<1 or HP>999):
    print("Must be between 1 and 999")
    HP = int(input("HP: "))
  MP = int(input("MP: "))
  while (MP<1 or MP>999):
    print("Must be between 1 and 999")
    MP = int(input("MP: "))
  row = [name, type, smove, HP, MP]
  leaderboard.append(row)

  print("== Beast added ==\n == MockeDex ==")
  counter=1
  for row in leaderboard:
    print(counter, end="\t")
    for item in row:
		    print(item, end="\t")
    print()
    counter+=1
  time.sleep(1000)
  os.system('clear')
  f = open("text.txt", "w")
  f.write(str(leaderboard))
  f.close()