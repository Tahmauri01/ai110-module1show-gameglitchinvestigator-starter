from logic_utils import get_range_for_difficulty


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
