
# Security Findings and Observations

## Assessment Context

- Target: OWASP Juice Shop
- URL: `http://127.0.0.1:3000`
- Environment: Kali Linux, Docker, and Burp Suite
- Scope: Local lab instance only

## Observation OBS-01: HTTP Response and Headers

**Test performed:** Sent an HTTP HEAD request using `curl -I`.

**Observed result:** The application returned `HTTP 200 OK` and HTTP response headers.

**Assessment:** This confirms the application responded to the request. The response alone does not establish whether the application is secure or vulnerable.

**Status:** Informational observation.

## Observation OBS-02: Login Response Behavior

**Test performed:** Submitted test login data through the local application and inspected the response in Burp Suite.

**Observed result:** The tested login request returned `HTTP 401 Unauthorized` with an invalid-credentials message.

**Assessment:** The tested request was not authenticated. This observation does not demonstrate an authentication bypass or establish that all authentication controls are secure.

**Status:** Informational observation.

## Observation OBS-03: Product Reviews API

**Request:** `GET /rest/products/1/reviews`

**Observed result:** Burp Repeater returned `HTTP 200 OK` with JSON review data associated with product ID 1.

**Assessment:** Product reviews may be intended for public access. The observed response alone does not demonstrate an insecure direct object reference (IDOR) or unauthorized access to private information.

**Status:** Informational observation.

## Confirmed Vulnerabilities

No vulnerability has been confirmed by the observations documented above.

Further controlled testing is required before reporting a vulnerability.

## Evidence

Supporting screenshots are stored in the `evidence/` directory, organized by day. Daily notes are stored in the `notes/` directory.

Before publishing evidence, verify that screenshots do not expose session cookies, tokens, passwords, or other sensitive information.

## General Recommendation

Continue testing within the authorized local lab. For any potential vulnerability, document the exact test, expected behavior, actual result, security impact, remediation, and retest outcome before assigning a severity.














FINDING-01: SQL Injection Authentication Bypass

Severity: High (preliminary, lab context)

Affected application:
OWASP Juice Shop - local intentionally vulnerable lab

Affected functionality:
Login authentication

Evidence:
The Login Admin challenge was marked as solved on the Score Board.
Screenshot: evidence/day5/D5-01-login-admin-solved.png

Security impact:
An attacker may bypass the login process and access an administrator
account if an application has the same vulnerability.

Root cause:
Potentially unsafe handling of user input in SQL authentication logic.

Recommended remediation:
- Use parameterized queries or prepared statements.
- Never concatenate untrusted input into SQL statements.
- Validate authentication on the server side.
- Add regression tests for authentication bypass attempts.

Validation status:
Confirmed in the intentionally vulnerable lab.
The severity is preliminary and has not been formally scored.
