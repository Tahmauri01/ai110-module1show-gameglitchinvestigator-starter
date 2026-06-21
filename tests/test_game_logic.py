from logic_utils import check_guess, update_score, get_range_for_difficulty


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


# --- Regression tests for the difficulty-range bug ---
# Hard should have the widest range and Easy the narrowest, and each
# difficulty must produce a distinct range. The original code gave Normal
# the widest range (1-100) and Hard only 1-50.

def _span(difficulty):
    low, high = get_range_for_difficulty(difficulty)
    return high - low


def test_each_difficulty_has_a_distinct_range():
    # Regression: switching difficulty used to leave the range unchanged.
    ranges = {
        d: get_range_for_difficulty(d) for d in ("Easy", "Normal", "Hard")
    }
    assert len(set(ranges.values())) == 3


def test_hard_has_the_largest_range():
    # Regression: Normal (1-100) used to be wider than Hard (1-50).
    assert _span("Hard") > _span("Normal") > _span("Easy")


def test_expected_range_values():
    assert get_range_for_difficulty("Easy") == (1, 20)
    assert get_range_for_difficulty("Normal") == (1, 50)
    assert get_range_for_difficulty("Hard") == (1, 100)
