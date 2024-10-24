from colorama import Fore, Back
import random
import time
import sys
import os


CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def clear_terminal():
    os.system("cls")


def slow_painting(text: str):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.04)


def deal_card():
    """ترد كارت عشوائي"""
    card = random.choice(CARDS)
    return card


def calculate_score(cards: list):
    "تأخذ قائمة من الكروت وتعيد لنا مجموعهم"""
    # هل الكروت فوق 21 وهناك رقم 11
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(user_score: int, computer_score: int, user_cards: list, computer_cards: list):
    results = {"draw": "Draw 😊 \n\n",
               "user_over": "You went over 21, Sorry \n\n",
               "computer_over": "Computer went over 21, you win \n\n",
               "user_21": "You won with a blackjack",
               "computer_21": "Sorry, computer had a blackjack \n\n",
               "user_win": "You win \n\n",
               "user_lose": "You lose \n\n",
               }

    if user_score == computer_score:
        return results["draw"]
    elif user_score == 21 and len (user_cards) == 2:
        return results["user_21"]
    elif computer_score == 21 and len (computer_cards) == 2:
        return results["computer_21"]
    elif user_score > 21:
        return results["user_over"]
    elif computer_score > 21:
        return results["computer_over"]
    elif user_score > computer_score:
        return results["user_win"]
    else:
        return results["user_lose"]


def game():
    user_cards = [deal_card() for _ in range(2)]
    computer_cards = [deal_card() for _ in range(2)]

    while True:
        # User's turn
        user_score = calculate_score(user_cards)
        slow_painting (f"\n\nYour cards are {user_cards}, with currently score {sum(user_cards)} \n")
        time.sleep(0.5)
        slow_painting (f"Computer's first card is {computer_cards[0]} \n")
        time.sleep(2)
        if user_score == 21 or computer_score == 21 or user_score > 21 or computer_score > 21:
           break
        else:
            user_needs_another_one = input ("Get another card? y/n ").lower()
            if user_needs_another_one == "y":
                user_cards.append(deal_card())
            else:
                break

    while computer_score < 17 and user_score < 21:
        # Computer's turn
        if user_score == 21 and len (user_cards) == 2:
           break
        else:
           computer_cards.append(deal_card())
           computer_score = calculate_score(computer_cards)
    
    print (f"Your final hand: {user_cards} with score {user_score}")
    time.sleep(1)
    slow_painting(f"Computer's final hand: {computer_cards} with score {computer_score} \n")
    time.sleep(0.4)
    slow_painting (compare(user_score, computer_score, user_cards, computer_cards))



while True:
    
    print(Back.BLACK) ## لتلوين الخلفية
    clear_terminal()  ##     بالكامل
    print(f"{Fore.WHITE} Choose a game to start ....\n\n1- Froggy \n2- Twenty one\n3- Snake \n------")
    quit() if input().lower() not in ("twenty one", "2") else clear_terminal()
    print("Starting game .......")
    time.sleep(2)
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
    game()
    time.sleep(3)
