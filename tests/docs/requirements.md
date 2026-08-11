# M-PESA Shield - System Requirements

## 1. Project Overview

M-PESA Shield is an independent educational application
designed to help users recognize suspicious digital messages
and learn safer digital-security practices.

The project is intended as a software-development and
cybersecurity-awareness portfolio project.

> IMPORTANT:
> M-PESA Shield is not an official Safaricom application
> and does not connect to Safaricom internal systems.

---

# 2. Problem Statement

Mobile and internet users may receive suspicious messages
that attempt to manipulate them into:

- Sharing security credentials
- Clicking suspicious links
- Sending money
- Responding to impersonators
- Acting under unnecessary pressure
- Believing fake rewards or account warnings

Users may not always recognize these warning signs.

M-PESA Shield provides an educational way to identify
common indicators and explain safer actions.

---

# 3. Project Objectives

The system should:

1. Allow users to enter a suspicious message.
2. Validate the submitted message.
3. Analyze the message using transparent rules.
4. Calculate an educational risk score.
5. Assign a risk category.
6. Explain detected warning indicators.
7. Provide safety recommendations.
8. Educate users about common social-engineering techniques.
9. Provide automated tests.
10. Maintain professional technical documentation.

---

# 4. Target Users

The initial target users are:

- Students
- Mobile-money users
- Digital-service users
- General internet users
- Users learning about cybersecurity awareness

---

# 5. Functional Requirements

## FR-01 - Message Input

The user shall be able to enter a message
for analysis.

---

## FR-02 - Input Validation

The system shall:

- Reject empty messages.
- Reject messages containing only whitespace.
- Limit message length.
- Validate incoming API requests.

---

## FR-03 - Message Analysis

The system shall inspect submitted messages
for configured warning indicators.

Examples include:

- PIN requests
- OTP requests
- Password requests
- Account-suspension threats
- Suspicious links
- Fake-prize language
- Money-transfer requests
- Verification requests

---

## FR-04 - Risk Score

The system shall generate an educational
risk score between 0 and 100.

---

## FR-05 - Risk Category

The system shall classify results into:

- LOW
- MEDIUM
- HIGH
- CRITICAL

---

## FR-06 - Explanation

The system shall explain why indicators were detected.

---

## FR-07 - Recommendations

The system shall provide safety recommendations
based on the identified risk level.

---

## FR-08 - Health Check

The backend shall provide a health-check endpoint
to confirm that the service is running.

---

## FR-09 - Error Handling

The application shall display understandable
error messages when requests fail.

---

## FR-10 - Testing

The project shall include automated tests for:

- Empty input
- Normal messages
- PIN requests
- OTP requests
- Password requests
- Suspicious links
- Multiple indicators
- Risk-score limits
- Case-insensitive detection

---

# 6. Non-Functional Requirements

## Performance

The application should return analysis results
quickly during normal local usage.

---

## Usability

The interface should be:

- Simple
- Clear
- Responsive
- Easy to navigate

---

## Accessibility

The application should use:

- Semantic HTML
- Labels for form controls
- Keyboard-accessible controls
- Readable text
- Clear error messages

---

## Maintainability

The code should be separated into logical components:

- Frontend
- Backend
- Analyzer
- Models
- Tests
- Documentation

---

## Security

The system should:

- Validate input.
- Avoid storing sensitive credentials.
- Avoid exposing secrets.
- Restrict development CORS configuration.
- Escape user-controlled output.
- Avoid logging private information.

---

# 7. Privacy Requirements

The application must not request or store:

- M-PESA PINs
- OTPs
- Passwords
- Authentication credentials
- Real customer financial information
- Private customer transaction records

The project should use synthetic examples
for demonstration and testing.

---

# 8. Technical Requirements

## Frontend

- HTML5
- CSS3
- JavaScript

## Backend

- Python
- FastAPI
- Pydantic

## Testing

- Pytest

## Development Tools

- Visual Studio Code
- Git
- GitHub

---

# 9. Project Limitations

Version 1 uses transparent rule-based analysis.

It does not:

- Connect to mobile-money systems.
- Access customer accounts.
- Access customer transaction databases.
- Access internal fraud-detection systems.
- Guarantee that a message is legitimate or fraudulent.

A LOW score does not prove that a message is safe.

A HIGH or CRITICAL score does not independently
prove that a message is fraudulent.

---

# 10. Future Requirements

Future versions may include:

- Natural-language processing
- Machine-learning experiments
- User reporting
- Authentication
- Admin dashboard
- Database integration
- Rate limiting
- Security monitoring
- CI/CD
- Cloud deployment
- Accessibility improvements
- Security testing automation