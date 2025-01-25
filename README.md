**Bulls and Cows Game**

Bulls and Cows is a classic number-guessing game where the player tries to guess a randomly generated 4-digit number. Each digit in the number is unique, and the first digit is never zero. The game provides feedback on each guess in the form of "bulls" and "cows":

- **Bulls**: Digits that match in both value and position.
- **Cows**: Digits that match in value but not in position.

**Features**

- Randomly generates a valid 4-digit number with unique digits.
- Validates user input to ensure it meets the game rules.
- Tracks and stores game statistics, including:
  - Total games played.
  - Best time to guess the correct number.
  - Best score (minimum number of guesses).
- Saves and loads game statistics from a JSON file.
- Friendly and intuitive text-based interface.

**Requirements**

No additional libraries are required, as the game uses only Python's built-in modules:

- random
- time
- json

**How to Play**

1. Clone or download the game script.
2. Run the script using Python:
3. python bulls_and_cows.py
4. Enter your name when prompted.
5. The game will generate a random 4-digit number. Your task is to guess it.
6. Enter a 4-digit number that follows these rules:
    - All digits must be unique.
    - The number cannot start with 0.
7. After each guess, the game will provide feedback:
    - The number of bulls (correct digits in the correct positions).
    - The number of cows (correct digits in incorrect positions).
8. Continue guessing until you find the correct number.
9. After completing a game, you can choose to play again or exit.

**Game Rules**

1. The generated number will always:
    - Be 4 digits long.
    - Have all unique digits.
    - Not start with the digit 0.
2. Input validation ensures:
    - The guess is exactly 4 digits long.
    - The guess contains only numeric characters.
    - The digits in the guess are unique.
3. Feedback:
    - Each guess provides the count of bulls and cows.
    - "4 bulls" indicates the correct guess and ends the game.

**Game Statistics**

The game keeps track of your performance and stores it in a JSON file named game_stats.json. Statistics include:

- **Best Time**: The fastest time to guess the number.
- **Best Score**: The minimum number of guesses required to guess the number.
- **Total Games Played**: The total number of games you have played.

These statistics are updated after each round and displayed at the end of the game, showing the best score and shortest time achieved.

**Code Overview**

**Main Functions**

1. **greet(name)** Greets the user with a personalized message.
2. **get_random_number()** Generates a random 4-digit number with unique digits.
3. **guess_a_number(guess)** Validates the user's guess according to game rules.
4. **get_bulls_and_cows(list_1, list_2)** Compares the generated number and the guessed number to calculate bulls and cows.
5. **load_game_stats(file_name)** Loads game statistics from a JSON file. If the file does not exist, initializes a default structure.
6. **save_game_stats(file_name)** Saves the current game statistics to a JSON file.
7. **play_game()** Contains the main game loop. Handles user input, feedback, and statistics updates.
8. **main_game_loop()** Repeats the game until the user decides to quit.

**File Handling**

The game stores statistics in game_stats.json. If the file is missing or corrupted, the game will create or reset it with default values.

Enjoy playing Bulls and Cows!
