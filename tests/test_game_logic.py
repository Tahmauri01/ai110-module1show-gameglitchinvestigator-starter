from logic_utils import check_guess, update_score


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high():
    # If secret is 50 and guess is 60, outcome should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low():
    # If secret is 50 and guess is 40, outcome should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# --- Regression tests for the inverted-hint bug ---
# A guess that is too high must tell the player to go LOWER, and a guess
# that is too low must tell them to go HIGHER. The original code had these
# messages swapped.

def test_too_high_hint_says_go_lower():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message.upper()
    assert "HIGHER" not in message.upper()


def test_too_low_hint_says_go_higher():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message.upper()
    # "HIGHER" contains "HIGH" but not "LOWER", so this guards the direction
    assert "LOWER" not in message.upper()


# --- Regression test for the inverted-score bug ---
# A "Too High" guess is a wrong guess and must always cost points, just like
# "Too Low". The original code rewarded +5 when the attempt number was even,
# letting players farm points by guessing too high on even attempts.

def test_too_high_on_even_attempt_loses_points():
    # Attempt 2 is even — this is the case that used to (wrongly) add +5.
    assert update_score(current_score=100, outcome="Too High", attempt_number=2) == 95


def test_too_high_penalty_matches_too_low():
    # Both wrong outcomes should change the score identically, regardless of
    # whether the attempt number is even or odd.
    for attempt in (1, 2, 3, 4):
        high = update_score(current_score=50, outcome="Too High", attempt_number=attempt)
        low = update_score(current_score=50, outcome="Too Low", attempt_number=attempt)
        assert high == low == 45
