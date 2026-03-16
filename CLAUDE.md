# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Run the app
python -m streamlit run app.py

# Install dependencies (uses venv or system pip)
pip install -r requirements.txt

# Run all tests
python -m pytest tests/

# Run a single test
python -m pytest tests/test_game_logic.py::test_winning_guess
```

## Architecture

This is a single-page Streamlit number-guessing game split into two layers:

- **`app.py`** — UI and session state only. Handles difficulty selection, guess input, button actions, win/loss detection, and score display. All game logic is delegated to `logic_utils.py`.
- **`logic_utils.py`** — Pure functions with no Streamlit dependency: `get_range_for_difficulty`, `parse_guess`, `check_guess`, `update_score`.
- **`tests/test_game_logic.py`** — pytest tests covering `check_guess` and `get_range_for_difficulty`. Tests import directly from `logic_utils`.

`check_guess` returns a tuple `(outcome, message)` where outcome is `"Win"`, `"Too High"`, or `"Too Low"`. `app.py` intentionally passes the secret as a string on even-numbered attempts (a deliberate bug for the exercise).

Session state keys used in `app.py`: `secret`, `attempts`, `score`, `status`, `history`.
