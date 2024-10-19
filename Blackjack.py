import random 
import time
import os

PLAYING_CARDS = [2,3,4,5,6,7,8,9,10,11]
                 
def clear_terminal():
    os.system("cls")

def random_card():
    return random.choice(PLAYING_CARDS)

def calculate_score(hand):
    if 11 in hand and sum(hand) > 21:
       hand.remove(11) 
       hand.append(1)

def main_menu():
    
    print ("Choose a game to start......")
    print ("\n1- Froggy \n2- Twenty one \n3- Snake \n------")
    quit() if input().lower() not in ("twenty one", "2") else clear_terminal()

    print ("Starting game .......")
    time.sleep(3)
    clear_terminal()
    
    print (r"""
       /\
     .'  `.
    '      `.
 .'          `.
{              }
 ~-...-||-...-~
       ||
      '--`

 _________          ________ _   _ _________     __    ____  _   _ ______
|__   __\ \        / /  ____| \ | |__   __\ \   / /   / __ \| \ | |  ____|
   | |   \ \  /\  / /| |__  |  \| |  | |   \ \_/ /   | |  | |  \| | |__
   | |    \ \/  \/ / |  __| |   ` |  | |    \   /    | |  | |   ` |  __|
   | |     \  /\  /  | |____| |\  |  | |     | |     | |__| | |\  | |____
   |_|      \/  \/   |______|_| \_|  |_|     |_|      \____/|_| \_|______|
                                                  ______   
                                                 |______|
""")

    run_project()

def run_project():
    def final_hand():
        print (f"\n \nYour final hand: {user_hand} with score {sum(user_hand)}")
        print (f"Computer final hand: {computer_hand} with score {sum(computer_hand)}")

    computer_hand = [random_card(), random_card()]
    user_hand = [random_card(), random_card()]
 
    while True: 
        
          calculate_score (computer_hand)
          calculate_score (user_hand)
         

          # The user points went over 21
          if sum (user_hand) > 21:
               final_hand()
               print ("You went over 21, computer win \n \n")
               break

          else:
               
               print (f"\n \nYour cards are {user_hand}, current score is {sum(user_hand)}")
               print (f"Computer's first card is {computer_hand [0]}")
               if input ("Get another card? y/n ").lower() == "y":
                  user_hand.append (random_card())
                  continue

               else:
                  while sum (computer_hand) <= 17:
                        if random.choice ([True , True, False]):

                           computer_hand.append (random_card())
                           calculate_score (computer_hand)

                        else:
                           break

                               
                  # The computer points went over 21
                  if sum (computer_hand) > 21:
                     final_hand()
                     print ("Computer went over 21, you win 🌟 \n \n") 
                     break

                  # The computer arrived to 21 points
                  elif sum (user_hand) == 21 and sum (computer_hand) < 21:
                       final_hand()
                       print ("You Win \n \n")
                       break 

                  # The computer arrived to 21 points
                  elif sum (computer_hand) == 21 and sum (user_hand) < 21:
                       final_hand()
                       print ("Computer Win \n \n")
                       break

                  # The computer and the user arrived to 21 points together
                  elif sum (computer_hand) == 21 and sum (user_hand) == 21:
                       final_hand()
                       print ("Draw \n \n")
                       break 
                        
                  # The computer has more points than the user at the end of the game
                  elif sum (computer_hand) < 21 and sum (user_hand) < 21 and sum (computer_hand) > sum (user_hand):
                       final_hand()
                       print ("Computer Win \n \n")
                       break

                  # The user has more points than the computer at the end of the game
                  elif sum (computer_hand) < 21 and sum (user_hand) < 21 and sum (user_hand) > sum (computer_hand):                  
                       final_hand()
                       print ("You Win \n \n")
                       break 

                  # The user and the computer have the same numbers of points at the end of the game
                  else:
                       final_hand()
                       print ("Draw \n \n")
                        

while True:
      main_menu()