# Vulnerability Assessment and Security Monitoring Lab

## 1. Executive Summary

This project combines web application security testing of a locally hosted OWASP Juice Shop instance with a basic Python-based security event detection exercise.

The VAPT activities included HTTP response inspection, Burp Suite traffic analysis, login testing, API inspection, and a SQL injection authentication-bypass challenge. The SOC exercise used simulated CSV login events to test a repeated-failed-login detection rule.

The Login Admin challenge was confirmed as solved in the local lab. The Python detection script passed one positive and one negative test using simulated data.

These results demonstrate lab testing and basic detection engineering. They do not establish that a production application is vulnerable or that a real attack was detected.

## 2. Scope and Environment

**Target:** OWASP Juice Shop

**Target URL:** `http://127.0.0.1:3000`

**Environment:** Kali Linux in Oracle VirtualBox, with Docker hosting Juice Shop.

**Tools:** Burp Suite, curl, Docker, and Python 3.

**Scope:** Testing was restricted to the local lab instance. The SOC detection exercise used simulated training data.

## 3. Methodology

The work performed included:

1. Inspecting HTTP responses and security-related headers.
2. Reviewing requests and responses using Burp Suite.
3. Testing login behavior with invalid dummy credentials.
4. Inspecting the product reviews API and other application responses.
5. Completing the Juice Shop Login Admin SQL injection challenge.
6. Reviewing available Docker container logs.
7. Creating simulated login-event datasets.
8. Developing and testing a Python detection script.
9. Recording observations, evidence, limitations, and remediation recommendations.

## 4. VAPT Observations

### 4.1 HTTP Responses and Headers

The application returned successful HTTP responses during baseline testing. Several security-related headers were observed.

These observations document application behavior; they do not independently establish a vulnerability.

### 4.2 Invalid Login Test

A login request using invalid dummy credentials returned `401 Unauthorized`.

This was expected behavior and did not demonstrate an authentication bypass.

### 4.3 Product Reviews API

The request `GET /rest/products/1/reviews` returned `200 OK` with JSON review data.

The response alone did not establish an IDOR or broken access control vulnerability.

### 4.4 CORS Observation

A wildcard `Access-Control-Allow-Origin` header was observed during testing.

The test did not establish exploitable CORS behavior or sensitive cross-origin data exposure. Further context-specific validation would be required before reporting this as a vulnerability.

## 5. Confirmed Lab Finding

### SQL Injection Authentication Bypass

**Affected application:** Local OWASP Juice Shop.

**Affected functionality:** Login authentication.

**Test result:** The Login Admin challenge was marked as solved after a SQL injection test.

**Evidence:** `evidence/day5/D5-01-login-admin-solved.png`

**Impact in the lab:** The test demonstrated authentication bypass and access to the administrator account in the intentionally vulnerable application.

**Severity:** Preliminary. No formal severity score has been calculated.

**Recommended remediation:**

- Use parameterized SQL queries or prepared statements.
- Avoid constructing SQL statements by concatenating untrusted input.
- Enforce server-side authentication and authorization checks.
- Add regression tests for authentication-bypass attempts.

**Scope limitation:** This finding was demonstrated in the local training application. It does not establish that any production application has the same vulnerability.

No source-code remediation was applied and verified as part of this project.

## 6. SOC Detection Exercise

### 6.1 Objective

Detect repeated failed login attempts from a single source IP address using a Python script.

### 6.2 Data Sources

The exercise used two simulated CSV datasets:

- `soc/data/login_events.csv`
- `soc/data/negative_test.csv`

These datasets were created for testing the detection logic. They are not real Juice Shop logs or evidence of an actual incident.

### 6.3 Detection Rule

Generate an alert when the same source IP address has five or more failed login attempts within a five-minute period.

### 6.4 Positive Test

**Dataset:** `soc/data/login_events.csv`

**Expected behavior:** Generate an alert for repeated failed logins.

**Observed result:** The script reported five failed logins within five minutes for `192.168.1.20`.

**Test status:** PASS.

### 6.5 Negative Test

**Dataset:** `soc/data/negative_test.csv`

**Expected behavior:** Do not generate an alert when the repeated-failure threshold is not reached.

**Observed result:** No repeated-failed-login alert was generated.

**Test status:** PASS.

### 6.6 Application Log Review

The Docker logs reviewed during the exercise contained startup and challenge-restoration messages. The collected output did not show the individual failed login attempt.

Consequently, the SOC detection was validated against simulated data rather than events collected from the Juice Shop application.

### 6.7 Recommended Analyst Response

If a similar alert occurred in a real environment, an analyst should:

1. Review the source IP address and affected accounts.
2. Correlate timestamps with authentication and endpoint logs.
3. Check for successful logins following repeated failures.
4. Determine whether the activity is malicious or a legitimate user error.
5. Recommend appropriate rate limiting, monitoring, and account protections.

The alert is an indicator for investigation, not proof of a brute-force attack.

## 7. Evidence and Project Files

- `README.md` — project overview and instructions.
- `findings.md` — security findings and observations.
- `final-report.md` — assessment and detection report.
- `notes/` — daily observations and SOC validation notes.
- `evidence/` — screenshots from lab testing.
- `soc/detect_failed_logins.py` — Python detection script.
- `soc/data/` — simulated training datasets.
- `soc/incident-report.md` — SOC investigation report.

## 8. Limitations

- Testing was limited to the intentionally vulnerable local application.
- The SQL injection finding applies to the lab challenge.
- The SOC datasets contain simulated events.
- The detection rule was tested against only a small number of examples.
- No real security incident was investigated.
- No production environment was assessed.
- The Juice Shop vulnerability was not patched and retested.
- The absence of an observed event in the collected Docker output does not prove that the application never logs such events.
- The project does not establish that the application is secure.

## 9. Conclusion

The project demonstrates practical beginner-level experience in web application testing, HTTP analysis, evidence handling, vulnerability documentation, Python-based event processing, basic detection logic, and SOC report writing.

The SQL injection authentication-bypass challenge was successfully completed in the local lab. The repeated-failed-login detection script passed its positive and negative tests on simulated datasets.

Further validation with representative security logs, additional detection test cases, and remediation verification would be required before treating these techniques as operational security controls.
