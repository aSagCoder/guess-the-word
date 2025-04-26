# Guess the Word Game

A simple command-line word guessing game where players try to guess a randomly selected word one letter at a time. The game fetches words dynamically from an online API and provides a fun and interactive experience.

## Features

- Fetches a list of words dynamically from the [Datamuse API](https://www.datamuse.com/api/).
- Tracks player statistics, including games played and games won.
- Allows players to:
  - Start a new game.
  - View their stats.
  - Quit the game.
- Provides feedback for correct and incorrect guesses.
- Limits the number of attempts to 10 per game.

## How to Play

1. Run the program.
2. Choose an option from the menu:
   - **Start Game**: Begin a new word guessing game.
   - **View Stats**: See your game statistics.
   - **Quit**: Exit the game.
3. During the game:
   - Guess one letter at a time.
   - You have 10 attempts to guess the word.
   - Correct guesses reveal the letter in the word.
   - Incorrect guesses reduce your remaining attempts.
4. Win by guessing the entire word before running out of attempts.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/<your-repo-name>.git
   ```
2. Navigate to the project directory:
   ```bash
   cd guess-the-word
   ```
3. Install dependencies (if applicable):
   ```bash
   npm install
   ```

## Usage

1. Start the game:
   ```bash
   npm start
   ```
2. Follow the on-screen instructions to guess the word.

## Technologies Used

- Language: [e.g., JavaScript, Python]
- Framework: [e.g., React, Flask]
- Tools: [e.g., Node.js, HTML/CSS]

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature-name"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- Inspiration: [Build a Word Guessing Game with Python](https://www.codedex.io/projects/build-a-word-guessing-game-with-python)
- Special thanks to contributors and testers.