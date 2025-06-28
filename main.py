from art import logo
import random

def play_game(chosen_num,lives):
    num_list=[]
    while lives!= 0:
        guess=int(input("Guess a number:"))
        if guess in num_list:
            print("Number Already guessed!!Try another number")
        else:
            num_list.append(guess)

        if guess == chosen_num:
            print("You Won !! Correct Guess .. Hurrayyy!!")
            break
        elif guess > chosen_num:
            print("Too High!!")
            lives-=1
            print(f"You have {lives} remaining attempts ")
        elif guess < chosen_num:
            print("Too low")
            lives-=1
            print(f"You have {lives} remaining attempts ")
    if lives == 0:
        print("You Lose!! Lost all your Livess :( \nBetter luck next time!")

computer_number=random.randint(1,100)
print(logo)
print("Welcome to the Number Guessing Game!!\nI'm thinking of a number between 1 and 100.")
difficulty_level=input("Enter your difficulty level:[easy/hard]:\n").lower()
if difficulty_level=="easy":
    life=10
    print("You have 10 attempts remaining to guess the number.")
    play_game(computer_number,life)
else:
    life=5
    play_game(computer_number,life)
