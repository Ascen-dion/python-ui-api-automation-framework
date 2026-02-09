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
                passed.append(line)

            if "::" in line and "FAILED" in line:
                failed.append(line)

    report = []
    report.append("Automation Test Report\n")
    report.append(f"Total Passed: {len(passed)}")
    report.append(f"Total Failed: {len(failed)}\n")

    if passed:
        report.append("PASSED TESTS:")
        report.extend(passed)
        report.append("")

    if failed:
        report.append("FAILED TESTS:")
        report.extend(failed)

    return "\n".join(report)


def send_email(report_text):
    sender = os.environ["EMAIL_SENDER"]
    password = os.environ["EMAIL_PASSWORD"]
    receiver = os.environ["EMAIL_RECEIVER"]

    msg = MIMEText(report_text)
    msg["Subject"] = "Automation Test Report"
    msg["From"] = sender
    msg["To"] = receiver

    with smtplib.SMTP("smtp.office365.com", 587) as server:
        server.starttls()
        server.login(sender, password)
        server.send_message(msg)


if __name__ == "__main__":
    report = parse_pytest_output("pytest-output.txt")
    send_email(report)
