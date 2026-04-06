# wordle-assessment 

This Python program is a command-line version of the Wordle game, where the user tries to guess a hidden five-letter word within a limited number of attempts. At the beginning of the program, the built-in random module is imported. This module provides functions for generating random values, and it is specifically used here to randomly choose the secret word from a list, ensuring that each time the game is played, a different word can be selected.



The program then reads from two external text files: target\_words.txt and all\_words.txt. These files are essential to how the game works. The target\_words.txt file contains a curated list of valid five-letter words that can be chosen as the secret word for the game. This ensures that only appropriate and intended words are used as answers. The all\_words.txt file, on the other hand, contains a much larger list of acceptable words that the player is allowed to guess. This includes all possible valid guesses, not just the ones that can be selected as the secret word. Both files are opened in read mode, and their contents are processed line by line using readlines(). A list comprehension is used along with strip() to remove newline characters and whitespace, resulting in two clean lists: target\_words (possible answers) and WORD\_LIST (valid guesses).



After loading the word lists, the program uses random.choice() to select one word from target\_words and stores it in the variable secret\_word. This is the word the player must guess. Two constants are also defined: MAX\_TRIES, which limits the player to six attempts, and WORD\_LENGTH, which ensures all guesses are exactly five letters long. These constants help enforce the rules of the game consistently.



The function give\_feedback(secret, guess) is responsible for comparing the user’s guess to the secret word and generating feedback. It starts by creating a list filled with underscores to represent each letter position. Both the secret word and the guess are converted into lists so they can be modified during processing. The function uses two loops: the first loop checks for letters that are correct and in the correct position, marking them as uppercase and removing them from further consideration. The second loop checks for letters that exist in the word but are in the wrong position, marking them as lowercase. This two-step process ensures accurate feedback, especially when dealing with repeated letters. The final result is joined into a string and returned.



The is\_valid\_word(word) function checks whether the user’s input is acceptable. It ensures the word is exactly five letters long and that it exists in WORD\_LIST (which comes from all\_words.txt). This prevents invalid inputs such as random strings or incorrectly sized words.



The main gameplay is handled in the play\_wordle() function. It displays instructions and then runs a loop for each attempt, up to the maximum number allowed. Within this loop, another loop ensures the user keeps entering input until a valid word is provided. Once a valid guess is entered, the program generates and displays feedback using the give\_feedback() function.



If the guess matches the secret\_word, the program congratulates the user and ends the game early. If the player uses all attempts without guessing correctly, the loop finishes and the correct word is revealed. This is handled using a for...else structure, where the else block runs only if the loop wasn’t exited early.



Finally, the if \_\_name\_\_ == "\_\_main\_\_": statement ensures that the game only runs when the script is executed directly, not when it is imported elsewhere. Overall, the program combines file handling, randomness, input validation, and logical comparisons to create a fully functional text-based word game.

