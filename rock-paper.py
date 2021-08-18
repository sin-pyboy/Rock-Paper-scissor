import random
def play():
  user =input("Enter your choice ! 'r' for rock , 'p' for paper , 's' for scissor \n")
  computer=random.choice(['r','p','s'])

  if user == computer:
    return "Tie !";
  if is_win(user,computer):
    return "you Won !"
  return "Computer Won ! Better luck next time"


def is_win(player,opponent):
  # r>s , s>p ,p>r
  if (player == 'r' and opponent == 'p') or (player == 's' and opponent =='p') or (player == 'p' and opponent == 'r'):
    return True;
print(play())
