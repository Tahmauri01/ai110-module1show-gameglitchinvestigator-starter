# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- A game to test your guessing skills while also being fun a interactive
- Game would tell you to "Go Lower" when you needed to go higher and vice versa, new game button did not work, score went up on some wrong guesses, guesses were sometimes read as a string, difficulies did not have the right attempt amounts or range, changing difficulies had no effect.
- Switched print messages for "Go Higher" and "Go Lower" hints, reset score, history, and status when new game button is pressed, removed feature where guesses that were even guesses turned into strings, changed the attempt amounts and ranges for each difficulty.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User enters a guess of 20
2. Game hint says guess is "Too low"
3. User enters a guess of 40
4. Game hint says guess is "Too high"
5. Every wrong guess subtracts points
6. The game ends when user runs out of attempts or guesses the correct number
7. User changes the difficulty on the left-hand side 
8. User presses new game to play again

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
========================== test session starts =========================
platform win32 -- Python 3.11.4, pytest-9.0.3, pluggy-1.6.0
rootdir: C:\Users\tmbo7\Downloads\ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.13.0
collected 10 items                                             


tests\test_game_logic py ..........                    [100%]

=========================== 10 passed in 0.05s =========================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
