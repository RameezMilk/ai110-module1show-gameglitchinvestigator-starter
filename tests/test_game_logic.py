from logic_utils import check_guess, get_range_for_difficulty

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"


def test_easy_returns_1_to_20():
    low, high = get_range_for_difficulty("Easy")
    assert low == 1
    assert high == 20


def test_normal_returns_1_to_50():
    low, high = get_range_for_difficulty("Normal")
    assert low == 1
    assert high == 50


def test_hard_returns_1_to_100():
    low, high = get_range_for_difficulty("Hard")
    assert low == 1
    assert high == 100


def test_unknown_difficulty_returns_1_to_100():
    low, high = get_range_for_difficulty("Unknown")
    assert low == 1
    assert high == 100


def test_hard_range_wider_than_normal():
    _, normal_high = get_range_for_difficulty("Normal")
    _, hard_high = get_range_for_difficulty("Hard")
    assert hard_high > normal_high


def test_normal_range_wider_than_easy():
    _, easy_high = get_range_for_difficulty("Easy")
    _, normal_high = get_range_for_difficulty("Normal")
    assert normal_high > easy_high


def test_all_ranges_start_at_1():
    for difficulty in ("Easy", "Normal", "Hard"):
        low, _ = get_range_for_difficulty(difficulty)
        assert low == 1, f"Expected low=1 for {difficulty}, got {low}"
