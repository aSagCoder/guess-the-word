import random
import requests

def fetch_word_bank():
    response = requests.get("https://api.datamuse.com/words?ml=game&max=10")
    if response.status_code == 200:
        words = [word['word'] for word in response.json()]
        return words
    else:
        print("Failed to fetch words from API.")
        return []

def play_game():
    word_bank = fetch_word_bank()
    if not word_bank:
        print("No words available.")
        return False

    word = random.choice(word_bank)
    guessedWord = ['_'] * len(word)
    attempts = 10

    while attempts > 0:
        print('\nCurrent word: ' + ' '.join(guessedWord))

        guess = input('Guess a letter: ').lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    guessedWord[i] = guess
            print('Great guess!')
        else:
            attempts -= 1
            print('Wrong guess! Attempts left: ' + str(attempts))

        if '_' not in guessedWord:
            print('\nCongratulations!! You guessed the word: ' + word)
            return True

    print('\nYou\'ve run out of attempts! The word was: ' + word)
    return False

def main():
    games_played = 0
    games_won = 0

    while True:
        print("\nMenu:")
        print("1. Start Game")
        print("2. View Stats")
        print("3. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            games_played += 1
            if play_game():
                games_won += 1
        elif choice == '2':
            print(f"\nPlayer Stats:")
            print(f"Games Played: {games_played}")
            print(f"Games Won: {games_won}")
        elif choice == '3':
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()