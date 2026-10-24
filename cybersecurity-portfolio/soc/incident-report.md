# SOC Investigation Report: Repeated Failed Logins

## 1. Objective

Develop and validate a basic detection rule for repeated failed login attempts from a single source IP address.

## 2. Scope

This exercise uses simulated CSV login events and a Python detection script. It is intended for learning and portfolio demonstration.

No real attack or production security incident was investigated.

## 3. Detection Rule

Generate an alert when the same source IP address has five or more failed login attempts within a five-minute period.

## 4. Investigation Results

### Positive Test

- Dataset: `soc/data/login_events.csv`
- Source IP: `192.168.1.20`
- Observed pattern: Five failed login attempts within five minutes
- Expected result: Alert generated
- Actual result: Alert generated
- Test status: PASS

### Negative Test

- Dataset: `soc/data/negative_test.csv`
- Observed pattern: One failed login, alongside ordinary login activity
- Expected result: No repeated-failure alert
- Actual result: No alert generated
- Test status: PASS

## 5. Analysis

The detection script correctly identified the repeated-failure pattern in the positive test dataset and did not alert on the selected negative test dataset.

Repeated login failures can indicate password guessing or brute-force activity. However, they can also result from a user repeatedly entering an incorrect password.

An alert should therefore initiate further investigation rather than be treated as proof of malicious activity.

## 6. Recommended Analyst Actions

1. Review the source IP address and the affected accounts.
2. Examine timestamps and correlate authentication events from relevant systems.
3. Check whether any successful login occurred after repeated failures.
4. Review additional evidence before classifying the activity as malicious.
5. Where appropriate, recommend rate limiting, monitoring, and account-protection controls.

## 7. Limitations

- The datasets contain simulated events.
- The detection has been tested against only a small number of examples.
- Real authentication logs have not yet been used to validate this rule.
- The detection does not establish the identity or intent of an actor.
- No automated blocking or account-lockout action was implemented.

## 8. Conclusion

The Python detection script passed the positive and negative tests performed with the simulated datasets. The exercise demonstrates basic event parsing, detection logic, validation, and incident-report writing.

Further validation with representative real logs is required before using this detection operationally.
