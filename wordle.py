import random 
"""
In the code,  when enavled, it will prompt the user to guess a five-letter word, in six attempts. 
The user will guess any five letter word, that are in the lists.
 If the guess is invalid, it will come up with: Invalid word. Please enter a valid 5-letter word from the list. 
 If the word is valid, the code will loop through, and prompt the user to guess the word again. 
 If letter is used in the word, it will be displayeed as either lowercase, if in correct spot, and uppercase, if letter is in the wrong spot
 If user guesses the word in six guesses, the game will congratulate the player and then the code wull exit the loop 
 If all attempts are used, without the user guessing the word, the word will be revealed
"""
target_words_file=open('target_words.txt','r')
all_words_file=open('all_words.txt','r')

target_words=[line.strip() for line in target_words_file.readlines()] 
WORD_LIST=[line.strip() for line in all_words_file.readlines()]

# print(target_words[:5])
# print(target_words[-5:])

# print(WORD_LIST[:5])
# print(WORD_LIST[-5:])

secret_word = random.choice(target_words)
MAX_TRIES = 6
WORD_LENGTH = 5

def give_feedback(secret, guess):
    result = ["_"] * WORD_LENGTH
    secret_chars = list(secret)
    guess_chars = list(guess)


    for i in range(WORD_LENGTH):
        if guess_chars[i] == secret_chars[i]:
            result[i] = guess_chars[i].upper()
            secret_chars[i] = None  
            guess_chars[i] = None

    
    for i in range(WORD_LENGTH):
        if guess_chars[i] is not None and guess_chars[i] in secret_chars:
            result[i] = guess_chars[i].lower()
            secret_chars[secret_chars.index(guess_chars[i])] = None

    return "".join(result)

def is_valid_word(word):
    return len(word) == WORD_LENGTH and word in WORD_LIST

def play_wordle():
    print("Welcome to Wordle!")
    print(f"Guess the {WORD_LENGTH}-letter word. You have {MAX_TRIES} tries.\n")

    for attempt in range(1, MAX_TRIES + 1):
        while True: 
            guess = input(f"Attempt {attempt}/{MAX_TRIES}: ").lower()
            if is_valid_word(guess):
                break
            else:
                print("Invalid word. Please enter a valid 5-letter word from the list.")

        feedback = give_feedback(secret_word, guess)
        print("Feedback:", feedback)

        if guess == secret_word:
            print(f"Congratulations! You guessed the word '{secret_word}' in {attempt} tries.")
            break
    else:
        print(f"Sorry, you've run out of attempts. The word was '{secret_word}'.")

if __name__ == "__main__":
    play_wordle()