"""
projekt_2.py: druhý projekt od Engeto Online Python Akademie

author: Kristýna Čadková
email: kristyna.posingerova@seznam.cz
discord: kristyna_90682
"""

import random
import time
import json


logo = r"""
  _           _ _                         
 | |         | | |                        
 | |__  _   _| | |___                     
 | '_ \| | | | | / __|                    
 | |_) | |_| | | \__ \                    
 |_.__/ \__,_|_|_|___/                    
         ___                              
        ( _ )        ___ _____      _____ 
        / _ \/\     / __/ _ \ \ /\ / / __|
       | (_>  <    | (_| (_) \ V  V /\__ \
        \___/\/     \___\___/ \_/\_/ |___/
"""

separator = 47 * "-"  # Divider for better readability

game_stats = {"duration": [], "score": [], "total_games": 0}  # Default structure for stats


def greet(name):
    """
    Greets the user with a personalized message.

    Args:
        name (str): The name of the user to greet.

    Returns:
        None
    """
    print(f"Hi {name}!")


def get_random_number():
    """
    Generates a 4-digit random number where all digits are unique,
    and the first digit is not zero.

    Returns:
        str: A string representing the random 4-digit number.
    """
    while True:
        random_number = random.sample(range(0, 10), k=4)
        if random_number[0] != 0:
            break
    return ''.join(map(str, random_number))


def guess_a_number(guess):
    """
    Validates a user's guessed number according to specific game rules.

    Args:
        guess (str): The user's guessed number as a string.

    Returns:
        str: The validated guess if it meets all criteria.
        None: If the guess does not meet the criteria, a message is printed, and None is returned.
    """
    if len(guess) != 4:
        print("Please, enter a 4-digit number.")
        return None
    if guess.startswith("0"):
        print("The number cannot start with 0.")
        return None
    if not guess.isdigit():
        print(f"{guess} is not a number.")
        return None
    if len(set(guess)) < 4:
        print("Duplicated digits are not allowed.")
        return None
    return guess


def get_bulls_and_cows(list_1, list_2):
    """
    Compares two lists of digits to calculate the number of bulls and cows.

    Bulls: Digits that match in both value and position.
    Cows: Digits that match in value but not in position.

    Args:
        list_1 (list): The target number as a list of digits.
        list_2 (list): The guessed number as a list of digits.

    Returns:
        list: A list of two integers - [bulls, cows].
    """
    bull_cow = [0, 0]
    for x, y in zip(list_1, list_2):
        if y in list_1:  # Digit exists
            if y == x:  # Match position and value
                bull_cow[0] += 1
            else:
                bull_cow[1] += 1  # Match value but not position
    return bull_cow


def load_game_stats(file_name="game_stats.json"):
    """
    Loads game statistics from a JSON file. If the file doesn't exist,
    initializes with a default structure.

    Args:
        file_name (str): The name of the file containing game statistics.

    Returns:
        dict: The loaded or initialized game statistics.
    """
    global game_stats
    try:
        with open(file_name, "r") as file:
            game_stats = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        game_stats = {"duration": [], "score": [], "total_games": 0}
    return game_stats


def save_game_stats(file_name="game_stats.json"):
    """
    Saves the current game statistics to a JSON file.

    Args:
        file_name (str): The name of the file to save game statistics to.

    Returns:
        None
    """
    with open(file_name, "w") as file:
        json.dump(game_stats, file)

def format_time(seconds):
    """
    Formats time in seconds to 'X min Y s' format if over 60 seconds,
    otherwise just 'X s'.

    Args:
        seconds (float): Time in seconds.

    Returns:
        str: Formatted time string.
    """
    minutes = int(seconds // 60)
    secs = round(seconds % 60)
    if minutes > 0:
        return f"{minutes} min {secs} s"
    else:
        return f"{secs} s"


def play_game():
    """
    Main gameplay loop for the Bulls and Cows game.
    Updates game statistics after the game ends.

    Returns:
        None
    """
    global game_stats

    random_number = get_random_number()
    #print(random_number)
    print(separator)
    print("I've generated a random 4-digit number for you.\nLet's play a Bulls and Cows game!")
    print(separator)

    guess_counter = 0
    start_time = time.time()

    while True:
        user_guess = input("Enter a number: ")
        guessed_number = guess_a_number(user_guess)
        if not guessed_number:
            continue

        guess_counter += 1
        bulls, cows = get_bulls_and_cows(list(random_number), list(guessed_number))
        
        if bulls == 1:
            bull_text = "bull"
        else:
            bull_text = "bulls"

        if cows == 1:
            cow_text = "cow"
        else:
            cow_text = "cows"
        
        print(f"{bulls} {bull_text}, {cows} {cow_text}\n{separator}")
        

        if bulls == 4:
            playing_time = round(time.time() - start_time, 2)
            formatted_time = format_time(playing_time)
            print(f"Correct! You've guessed the right number in {guess_counter} guesses and {formatted_time}!")
            game_stats["score"].append(guess_counter)
            game_stats["duration"].append(playing_time)
            game_stats["total_games"] += 1
            save_game_stats()
            print(f"Best score: {min(game_stats['score'])} guesses\nBest time: {format_time(min(game_stats['duration']))}")
            break



def game_loop():
    """
    Repeats the Bulls and Cows game until the user decides to quit.

    Returns:
        None
    """
    while True:
        play_game()
        repeat = input("Do you want to play again? (yes/no): ").strip().lower()
        if repeat != "yes":
            print(f"Great job, {username}! Come back soon to beat your high score!")
            break


# play the game
load_game_stats()
print(logo)
username = input("Enter your name: ")
greet(username)
game_loop()

