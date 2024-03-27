"""
SCORE A GAME by codecademy: SCRABBLE LAB.

TABLE: Player and their word

player1	wordNerd	Lexi Con	Prof Reader
BLUEMAN	EARTH	    ERASER	        ZAP
TENNIS	EYES	    BELLY	        COMA
EXIT	MACHINE	    HUSKY	        PERIOD

Result:
WINNER OF THIS GAME:
one who scores the most

"""
player_to_words = {
    "player1": ["BLUEMAN", "TENNIS", "EXIT"],
    "wordNerd": ["EARTH", "EYES", "MACHINE"],
    "Lexi Con": ["ERASER", "BELLY", "HUSKY"],
    "Prof Reader": ["ZAP", "COMA", "PERIOD"],
}
new_player_to_words = {
    "player2": ["blueman", "tennis", "EXIT"],
    "wordNerd2": ["EARTH", "EYES", "MACHINE"],
    "Lexi Con2": ["ERASER", "BELLY", "HUSKY"],
    "Prof Reader2": ["ZAP", "COMA", "period"],
}

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letters_to_points = {letter:point for letter, point in zip(letters, points)}

letters_to_points[''] = 0 # add '': 0 in dictionary as well

# print(letters_to_points)

def change_word_to_uppercase(word):
    return word.upper()

def score_word(word):
    word = change_word_to_uppercase(word)
    return sum(letters_to_points[letter] for letter in word)

def score_player(words_list):
    return sum(score_word(word) for word in words_list)

def update_points_total(player_to_words):
    return {player:score_player(word_list) for player, word_list in player_to_words.items()}

# player_to_points = update_points_total(player_to_words)
# print(player_to_points)

def get_winner(player_to_words):
    player_to_points = update_points_total(player_to_words)
    highest_score = max(player_to_points.values())
    winner = ''
    for player,score in player_to_points.items():
        if score == highest_score:
            winner = player
    return winner, highest_score


def display_winner(player_to_words):
    winner_name, winner_score = get_winner(player_to_words)
    print(f"Winner of game is {winner_name} with score {winner_score}")

display_winner(player_to_words)

display_winner(new_player_to_words)

"""
PS: I refactored few code statements after learning list and dict comprehension and pure functions.
"""

"""
CODE REVIEW BY CHATGPT:
-- I will refactor my code based on following review:

Consistent Naming: Ensure consistent naming conventions for variables, functions, and data structures throughout the codebase. Choose a naming convention and apply it uniformly.

Documentation: Add docstrings to functions to describe their purpose, parameters, and return values. Proper documentation enhances code readability and helps other developers understand the codebase more easily.

Error Handling: Implement robust error handling mechanisms to gracefully handle unexpected inputs or edge cases. Consider scenarios such as empty word lists, non-alphabetic characters in words, or missing keys in dictionaries.

Test Cases: Write comprehensive test cases to validate the correctness of functions. Include test cases for various scenarios, such as valid word combinations, empty input dictionaries, and edge cases. Ensure thorough testing to verify the behavior of functions under different conditions.

Efficiency Optimization: Assess the code for opportunities to improve performance and efficiency. Look for ways to streamline the code, optimize algorithms, or utilize more efficient data structures. Ensure that the code performs well, especially with large datasets.

Acceptance Criteria:

Consistent naming conventions applied throughout the codebase.
Functions documented with appropriate docstrings describing their purpose, parameters, and return values.
Robust error handling implemented to handle unexpected inputs or edge cases gracefully.
Comprehensive test suite covering various scenarios and edge cases.
Code optimized for efficiency without sacrificing readability or maintainability.
"""