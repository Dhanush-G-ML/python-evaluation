"""Grade helpers for a small training course. This is the code under test: do not change it."""


def _check_score(score):
    if isinstance(score, bool) or not isinstance(score, (int, float)):
        raise TypeError("score must be a number")
    if score < 0 or score > 100:
        raise ValueError("score must be between 0 and 100")


def percent_to_grade(score):
    """Return A (90+), B (80+), C (70+), D (60+) or F for a score from 0 to 100."""
    _check_score(score)
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"


def average(scores):
    """Return the mean of a non-empty list of scores."""
    if not scores:
        raise ValueError("no scores to average")
    for score in scores:
        _check_score(score)
    return sum(scores) / len(scores)


def has_passed(score, pass_mark=50):
    """Return True when the score is at or above the pass mark."""
    _check_score(score)
    return score >= pass_mark
