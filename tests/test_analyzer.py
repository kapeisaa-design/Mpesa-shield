import sys
from pathlib import Path

import pytest


# Add the backend directory to Python's import path
# so that the analyzer module can be tested.
BACKEND_DIRECTORY = (
    Path(__file__).resolve().parents[1] / "backend"
)

sys.path.append(str(BACKEND_DIRECTORY))


from analyzer import analyze_message


def test_empty_message_is_rejected():
    """Empty messages should not be accepted."""

    with pytest.raises(ValueError):
        analyze_message("")


def test_whitespace_message_is_rejected():
    """Messages containing only spaces should be rejected."""

    with pytest.raises(ValueError):
        analyze_message("     ")


def test_pin_request_is_detected():
    """A request for a PIN should increase the risk score."""

    result = analyze_message(
        "Please send your PIN immediately."
    )

    assert result.score >= 40
    assert len(result.reasons) > 0


def test_otp_request_is_detected():
    """A request for an OTP should increase the risk score."""

    result = analyze_message(
        "Provide your OTP to verify your account."
    )

    assert result.score >= 40
    assert len(result.reasons) > 0


def test_password_request_is_detected():
    """A password request should increase the risk score."""

    result = analyze_message(
        "Please send your password to verify your account."
    )

    assert result.score >= 40


def test_normal_message_has_low_risk():
    """A normal message should receive a low risk score."""

    result = analyze_message(
        "The meeting starts at 10am tomorrow."
    )

    assert result.category == "LOW"
    assert result.score < 25


def test_suspicious_account_message():
    """Account threats should be detected."""

    result = analyze_message(
        "Your account will be suspended."
    )

    assert result.score >= 20


def test_suspicious_link_is_detected():
    """Messages encouraging users to click links should be detected."""

    result = analyze_message(
        "Click this link to verify your account."
    )

    assert result.score >= 25


def test_multiple_indicators_increase_risk():
    """Multiple suspicious indicators should produce higher risk."""

    result = analyze_message(
        "Your account will be suspended. "
        "Send your PIN and click this link."
    )

    assert result.score >= 75
    assert result.category == "CRITICAL"


def test_score_never_exceeds_100():
    """Risk score must never exceed 100."""

    result = analyze_message(
        "PIN OTP password account suspended "
        "click this link claim your prize "
        "verify your account send money"
    )

    assert result.score <= 100


def test_result_contains_recommendations():
    """Every analysis should provide safety recommendations."""

    result = analyze_message(
        "Please send your PIN."
    )

    assert len(result.recommendations) > 0


def test_case_insensitivity():
    """Detection should work regardless of letter casing."""

    result = analyze_message(
        "PLEASE SEND YOUR PIN."
    )

    assert result.score >= 40

def test_alternative_link_wording_is_detected():
    result = analyze_message(
        "You are clicking here to verify your account."
    )

    assert result.score == 40
    assert result.category == "MEDIUM"


def test_tap_here_is_detected():
    result = analyze_message(
        "Tap here to verify your account."
    )

    assert result.score == 40
    assert result.category == "MEDIUM"


def test_open_this_link_is_detected():
    result = analyze_message(
        "Open this link to claim your prize."
    )

    assert result.score == 45
    assert result.category == "MEDIUM"


def test_prize_scam_with_clicking_here_is_high_risk():
    result = analyze_message(
        "Congratulations! You have won a prize. "
        "Claim your prize by clicking here."
    )

    assert result.score == 65
    assert result.category == "HIGH"
