# wordle-assessment

This Python program is a command-line version of the Wordle game, where the user tries to guess a hidden five-letter word within a limited number of attempts. At the very start, the program imports the built-in random module. This module provides functions for generating random values, and in this case it is specifically used to randomly select the secret word from a list so that each game is different.



The program then opens two text files using the open() function in read mode ('r'). The file target\_words.txt contains the list of possible secret words, while all\_words.txt contains all valid guesses the player is allowed to enter. The contents of these files are read line by line using the readlines() method. A list comprehension is used to process each line, where line.strip() removes any extra whitespace or newline characters. This results in two clean lists of words: target\_words and WORD\_LIST.



Next, the program randomly selects one word from the target\_words list using random.choice() and stores it in the variable secret\_word. This is the word the player must guess. Two constants are also defined: MAX\_TRIES, which limits the player to six attempts, and WORD\_LENGTH, which ensures that all guesses must be exactly five letters long. These constants are used throughout the program to keep the rules consistent.



The function give\_feedback(secret, guess) is responsible for comparing the player’s guess to the secret word and generating feedback. It starts by creating a list called result, filled with underscores, which represent each letter position. Both the secret word and the guess are converted into lists of characters so they can be modified during processing. The function uses two loops. The first loop checks each position to see if the guessed letter exactly matches the secret letter. If it does, that letter is added to the result in uppercase, and both the secret and guess positions are set to None so they are not reused. The second loop checks for letters that exist in the secret word but are in the wrong position. These letters are added in lowercase, and once matched, they are removed from the secret list to avoid counting duplicates. Finally, the result list is joined into a single string and returned as feedback.



The is\_valid\_word(word) function checks whether the user’s input is acceptable. It ensures the word is exactly five letters long and that it exists in the WORD\_LIST. This prevents invalid guesses and ensures the game only accepts real words from the provided list.



The main gameplay takes place in the play\_wordle() function. It begins by printing instructions for the user. A loop runs from 1 to MAX\_TRIES, representing each attempt. Inside this loop, there is another loop that repeatedly asks the user to input a guess until a valid word is entered. Once a valid guess is received, the program calls give\_feedback() to generate feedback and prints it.



If the user’s guess matches the secret word, the program prints a congratulatory message and stops the game early using break. If the user does not guess the word within the allowed attempts, the loop completes normally, and the program reveals the correct word. This is handled using a for...else structure, where the else block only executes if the loop was not exited early.



Finally, the line if \_\_name\_\_ == "\_\_main\_\_": ensures that the play\_wordle() function only runs when the script is executed directly, and not if it is imported into another program. Overall, the code demonstrates how file handling, random selection, loops, conditionals, and functions work together to create an interactive text-based game.

