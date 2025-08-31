import imaplib, email
from dotenv import load_dotenv
import os

load_dotenv()

EMAIL = os.getenv("EMAIL_ADDRESS")
PASSWORD = os.getenv("EMAIL_PASSWORD")
IMAP_SERVER = os.getenv("IMAP_SERVER")


def fetch_latest_emails(limit=2):
    mail = imaplib.IMAP4_SSL(IMAP_SERVER)
    mail.login(EMAIL, PASSWORD)
    mail.select("inbox")
    _, data = mail.search(None, "UNSEEN")
    mail_ids = data[0].split()[-limit:]

    emails = []
    for num in mail_ids:
        _, data = mail.fetch(num, "(RFC822)")
        msg = email.message_from_bytes(data[0][1])
        body = ""
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    body += part.get_payload(decode=True).decode()
        else:
            body = msg.get_payload(decode=True).decode()
        emails.append({"from": msg["from"], "subject": msg["subject"], "body": body})
    return emails
