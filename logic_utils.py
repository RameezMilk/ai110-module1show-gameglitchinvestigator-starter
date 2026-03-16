# Bug: The return ranges for "Normal" and "Hard" were swapped. "Normal" was returning (1, 50)
# and "Hard" was returning (1, 100), when it should be the other way around — a harder
# difficulty should have a wider range, making the number harder to guess.
# Fix: Swapped the return values so "Normal" returns (1, 50) and "Hard" returns (1, 100).
# Author: Rameez Malik + Claude Code
def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 50
    if difficulty == "Hard":
        return 1, 100
    return 1, 100

def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


# Bug: The hint messages for "Too High" and "Too Low" were swapped. When the guess was too
# high, the message said "Go HIGHER!" and when too low it said "Go LOWER!", which is the
# opposite of correct. Additionally, app.py was casting the secret to a string on even-numbered
# attempts, causing string comparison instead of numeric, producing inconsistent results.
# Fix: Swapped the messages so "Too High" returns "Go LOWER!" and "Too Low" returns "Go HIGHER!".
# Removed the string-cast logic from app.py so the secret is always passed as an int.
# Author: Rameez Malik + Claude Code
def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    if guess == secret:
        return "Win", "🎉 Correct!"

    try:
        if guess > secret:
            return "Too High", "📉 Go LOWER!"
        else:
            return "Too Low", "📈 Go HIGHER!"
    except TypeError:
        g = str(guess)
        if g == secret:
            return "Win", "🎉 Correct!"
        if g > secret:
            return "Too High", "📉 Go LOWER!"
        return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
