from random import randint
welcome_banner = """
                Welcome to Odds and Evens!

    This game simulates a hand game between two 
    players. Each player holds up a hidden amount
    of fingers on one hand. One player chooses 
    whether the sum will be "odd" or "even". Then,
    each player shows their hand, and you take the
    total of the number of fingers and see who wins.

    For example, if player1 chooses "odd" and the
    sum of the fingers is 4, player1 loses.
"""

print(welcome_banner)
player_name = input("What is your name?")
num_player_fingers = input("How many fingers do you want to hold up?")
num_computer_fingers = randint(1,5)
if num_player_fingers < 1 or num_player_fingers > 5:
    print("Invalid number?!")
    num_player_fingers = randint(1,5)
    
    player_choice = randint(1,5)
if player_choice != "odd" and player_choice !=  "even":
    print("Invalid choice?!")
    player_choice = "even"
