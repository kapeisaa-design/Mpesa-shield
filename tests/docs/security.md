# M-PESA Shield - Security Considerations

## 1. Security Purpose

Security is a core requirement of M-PESA Shield.

The application is designed as an educational project
and should demonstrate secure development practices.

---

# 2. Important Disclaimer

M-PESA Shield is an independent educational project.

It is NOT an official Safaricom application.

The project does not connect to:

- Safaricom internal systems
- Customer databases
- M-PESA customer accounts
- Internal fraud-detection systems
- Customer transaction systems

---

# 3. Sensitive Information

Users must never submit:

- M-PESA PINs
- OTPs
- Passwords
- Authentication tokens
- Account credentials
- Bank-card information
- Private financial information
- Real customer transaction information

Testing should use fictional examples.

---

# 4. Input Validation

The backend validates incoming data using Pydantic.

The application:

- Rejects empty messages.
- Rejects whitespace-only messages.
- Limits message length.
- Rejects malformed API requests.

The current maximum message length is:

```text
2000 characters