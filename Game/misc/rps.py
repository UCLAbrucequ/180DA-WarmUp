import random
import pygame
import Constants



def play(input1, input2):
    # while True:
    user_action = input2
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = input1
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

        # play_again = input("Play again? (y/n): ")
        # if play_again.lower() != "y":
        #     break


def display(user1, user2):
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    screen.fill((0, 0, 0))
    while True:
        pygame.display.flip()  # do your non-blocked other stuff here, like receive IMU data or something.

        if Constants.show_rock:
            pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

        

