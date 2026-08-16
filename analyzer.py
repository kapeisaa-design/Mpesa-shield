from dataclasses import dataclass
from typing import List


@dataclass
class AnalysisResult:
    """Represents the result returned by the message analyzer."""

    score: int
    category: str
    reasons: List[str]
    recommendations: List[str]


# These are educational indicators only.
# They do NOT represent Safaricom's internal fraud-detection rules.
SUSPICIOUS_PATTERNS = {
    "pin": {
        "weight": 40,
        "reason": (
            "The message appears to request a PIN "
            "or security credential."
        ),
    },

    "otp": {
        "weight": 40,
        "reason": (
            "The message appears to request an OTP "
            "or verification code."
        ),
    },

    "password": {
        "weight": 40,
        "reason": (
            "The message appears to request a password."
        ),
    },

    "suspended": {
        "weight": 20,
        "reason": (
            "The message uses an account-suspension "
            "threat to create urgency."
        ),
    },

    "click this link": {
        "weight": 25,
        "reason": (
            "The message encourages the user to click a link."
        ),
    },

    "claim your prize": {
        "weight": 20,
        "reason": (
            "The message uses a prize or reward "
            "to encourage action."
        ),
    },

    "verify your account": {
        "weight": 15,
        "reason": (
            "The message asks the user to verify an account."
        ),
    },

    "send money": {
        "weight": 20,
        "reason": (
            "The message appears to request a money transfer."
        ),
    },

    "click the link": {
        "weight": 25,
        "reason": (
            "The message encourages the user to click a link."
        ),
    },

    "click here": {
        "weight": 25,
        "reason": (
            "The message encourages the user to click a link."
        ),
    },

   "blocked": {
    "weight": 20,
    "reason": (
        "The message uses an account-blocking "
        "threat to create urgency."
    ),
},

    "transfer cash": {
        "weight": 20,
        "reason": (
            "The message appears to request a cash transfer."
        ),
    },

    "you have won": {
        "weight": 20,
        "reason": (
            "The message claims that the user has won "
            "a prize or reward."
        ),
    },
}


def get_category(score: int) -> str:
    """Convert a numerical score into a risk category."""

    if score >= 75:
        return "CRITICAL"

    if score >= 50:
        return "HIGH"

    if score >= 25:
        return "MEDIUM"

    return "LOW"


def get_recommendations(category: str) -> List[str]:
    """Generate safety recommendations based on risk level."""

    if category == "CRITICAL":
        return [
            "Stop interacting with the message.",
            "Do not provide your PIN, OTP, password or other security credentials.",
            "Verify the situation using an official customer-support channel.",
        ]

    if category == "HIGH":
        return [
            "Do not respond until the sender is verified.",
            "Never share your PIN, OTP or password.",
            "Verify the information through an official channel.",
        ]

    if category == "MEDIUM":
        return [
            "Be cautious before taking action.",
            "Verify the sender and information independently.",
            "Do not disclose security credentials.",
        ]

    return [
        "No strong scam indicators were detected.",
        "Continue protecting your PIN, OTP and passwords.",
        "Be cautious with unexpected messages or links.",
    ]


def analyze_message(message: str) -> AnalysisResult:
    """
    Analyze a message using transparent educational rules.
    """

    if not isinstance(message, str):
        raise ValueError("Message must be text.")

    normalized_message = message.lower().strip()

    if not normalized_message:
        raise ValueError("Message cannot be empty.")

    score = 0
    reasons = []

    for pattern, details in SUSPICIOUS_PATTERNS.items():

        if pattern in normalized_message:

            score += details["weight"]

            reasons.append(
                details["reason"]
            )

    # Prevent the score from exceeding 100.
    score = min(score, 100)

    category = get_category(score)

    recommendations = get_recommendations(
        category
    )

    if not reasons:
        reasons.append(
            "No configured suspicious indicators "
            "were detected in this message."
        )

    return AnalysisResult(
        score=score,
        category=category,
        reasons=reasons,
        recommendations=recommendations,
    )
