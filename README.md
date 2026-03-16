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

- [x] **Game's purpose:** A number guessing game built with Streamlit where the player picks a difficulty, gets a range, and tries to guess the secret number within a limited number of attempts. Hints guide you higher or lower after each guess and a score is tracked throughout.

- [x] **Bugs found:**
  1. The difficulty ranges for Normal and Hard were swapped — Normal was returning 1–100 and Hard was returning 1–50, when it should be the other way around.
  2. The hint messages in `check_guess` were swapped — guessing too high told you to go higher, and guessing too low told you to go lower.
  3. In `app.py`, on even-numbered attempts the secret was cast to a string, causing string-based comparison instead of numeric, which made hints appear random and inconsistent.

- [x] **Fixes applied:**
  1. Swapped the return values in `get_range_for_difficulty` so Normal returns (1, 50) and Hard returns (1, 100).
  2. Fixed the hint messages in `check_guess` so "Too High" says "Go LOWER!" and "Too Low" says "Go HIGHER!".
  3. Removed the even-attempt string cast in `app.py` so the secret is always passed as an int to `check_guess`.
  4. Added pytests in `tests/test_game_logic.py` to cover all three fixes and prevent regression.

## 📸 Demo

- [x] (screenshots/winning_screenshot.png)

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
