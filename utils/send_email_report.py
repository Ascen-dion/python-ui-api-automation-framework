import os
import smtplib
from email.mime.text import MIMEText


def parse_pytest_output(file_path):
    passed = []
    failed = []

    with open(file_path, "r") as f:
        for line in f:
            line = line.strip()

            if "::" in line and "PASSED" in line:
                test_name = line.split(" ")[0]
                passed.append(test_name)

            if "::" in line and "FAILED" in line:
                test_name = line.split(" ")[0]
                failed.append(test_name)

    report = []
    report.append("AUTOMATION TEST REPORT\n")
    report.append(f"Total Passed: {len(passed)}")
    report.append(f"Total Failed: {len(failed)}\n")

    if passed:
        report.append("PASSED TEST CASES:")
        report.extend(f"  - {t}" for t in passed)
        report.append("")

    if failed:
        report.append("FAILED TEST CASES:")
        report.extend(f"  - {t}" for t in failed)

    return "\n".join(report)


def send_email(report_text):
    sender = os.environ["EMAIL_SENDER"]
    password = os.environ["EMAIL_PASSWORD"]

    receivers = os.environ["EMAIL_RECEIVER"].split(",")
    receivers = [r.strip() for r in receivers if r.strip()]

    msg = MIMEText(report_text)
    msg["Subject"] = "Automation Test Report"
    msg["From"] = sender
    msg["To"] = ", ".join(receivers)

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, receivers, msg.as_string())

if __name__ == "__main__":
    report = parse_pytest_output("pytest-output.txt")
    send_email(report)
