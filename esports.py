leaderboard = []

while(True):
  name = input("Name: ")
  email = input("Email: ")
  bestScore = int(input("Best Score: "))

  row = [name, email, bestScore]
  leaderboard.append(row)
  print(leaderboard)