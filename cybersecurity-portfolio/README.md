# Vulnerability Assessment and Security Monitoring Lab

## 1. Project Overview

This project demonstrates beginner-level web application security testing and security event detection in a controlled Kali Linux lab. It combines OWASP Juice Shop testing with a Python-based SOC detection exercise.

## 2. Objectives

- Analyze HTTP requests and responses using Burp Suite.
- Inspect web application endpoints and API responses.
- Test authentication behavior in an intentionally vulnerable application.
- Document findings, evidence, limitations, and remediation recommendations.
- Develop and validate a basic repeated-failed-login detection rule.
- Practice writing a SOC investigation report.

## 3. Lab Environment

- Operating system: Kali Linux
- Virtualization: Oracle VirtualBox
- Target application: OWASP Juice Shop
- Container platform: Docker
- Web testing tool: Burp Suite
- Command-line tool: curl
- Programming language: Python 3

## 4. Scope

VAPT testing was performed against the locally hosted OWASP Juice Shop application:

`http://127.0.0.1:3000`

The SOC detection exercise uses simulated CSV login events. These events are not real Juice Shop logs.

Testing was restricted to the local lab.

## 5. VAPT Activities

- Inspected HTTP responses and security-related headers.
- Examined requests and responses in Burp Suite.
- Tested invalid login behavior.
- Inspected the application language endpoint and product reviews API.
- Observed CORS response headers.
- Completed the Juice Shop Login Admin SQL injection challenge.
- Saved screenshots and documented test observations.

### Confirmed Lab Finding

The Login Admin challenge was marked as solved after a SQL injection test. This demonstrates authentication bypass in the intentionally vulnerable Juice Shop lab.

Evidence:

`evidence/day5/D5-01-login-admin-solved.png`

Recommended remediation includes parameterized SQL queries, avoiding unsafe SQL construction, and enforcing server-side authentication and authorization.

This result does not establish that a production application has the same vulnerability.

Other observations, such as an HTTP 401 response, a public API response, or a wildcard CORS header, have not independently established additional vulnerabilities.

## 6. SOC Detection Exercise

A Python script was developed at:

`soc/detect_failed_logins.py`

The script analyzes CSV login events and generates an alert when the same source IP address has five or more failed login attempts within five minutes.

### Test Results

**Positive test**

- Dataset: `soc/data/login_events.csv`
- Expected behavior: Alert on repeated failed logins.
- Observed behavior: Alert generated for `192.168.1.20`.
- Result: PASS.

**Negative test**

- Dataset: `soc/data/negative_test.csv`
- Expected behavior: No alert when the repeated-failure threshold is not reached.
- Observed behavior: No alert generated.
- Result: PASS.

Both datasets contain simulated training events. These tests validate the script against the selected examples; they do not demonstrate detection of a real attack.

The application Docker logs reviewed during the exercise did not show the individual failed login event in the collected output.

## 7. Project Structure

- `evidence/` — screenshots from lab testing
- `notes/` — VAPT observations and SOC investigation notes
- `soc/data/` — simulated positive and negative test datasets
- `soc/detect_failed_logins.py` — Python detection script
- `soc/incident-report.md` — SOC investigation report
- `findings.md` — security findings and observations
- `final-report.md` — overall assessment report
- `README.md` — project overview and instructions

## 8. Limitations

- Testing was limited to an intentionally vulnerable local application.
- The SQL injection result applies to the lab challenge.
- The simulated SOC datasets are not production logs.
- The detection rule has been tested against a small number of examples.
- No production incident was investigated.
- No remediation was applied to the Juice Shop source code and verified.
- The assessment does not establish that the application is secure.

## 9. Learning Outcomes

This project demonstrates practical experience with HTTP analysis, Burp Suite, API inspection, authentication testing, evidence documentation, Python CSV processing, basic security detection logic, positive and negative testing, and SOC report writing.
