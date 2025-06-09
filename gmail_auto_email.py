# email_automation.py
import csv
import time
import pickle
import os.path
from email.mime.text import MIMEText
import base64
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request

SCOPES = ['https://www.googleapis.com/auth/gmail.send']
TOKEN_PICKLE = 'token.pickle'
CREDS_FILE = 'credentials.json'


def get_credentials():
    creds = None
    if os.path.exists(TOKEN_PICKLE):
        with open(TOKEN_PICKLE, 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(TOKEN_PICKLE, 'wb') as token:
            pickle.dump(creds, token)
    return creds


def create_message(sender, to, subject, message_text):
    message = MIMEText(message_text)
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
    return {'raw': raw}


def send_email(service, sender, to, subject, body):
    message = create_message(sender, to, subject, body)
    sent_message = service.users().messages().send(userId='me', body=message).execute()
    print(f"Email sent to {to}")
    return sent_message


def main():
    creds = get_credentials()
    service = build('gmail', 'v1', credentials=creds)

    with open('contacts.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        with open('message.txt', 'r', encoding='utf-8') as f:
            template = f.read()

        for row in reader:
            name = row['Name']
            email = row['Email']
            company = row['Company']

            print(f"\nReady to email: {name} at {email} ({company})")
            confirm = input("Send this email? (yes/no): ").strip().lower()
            if confirm != 'yes':
                print("Skipped.")
                continue

            personalized_message = template.replace('{name}', name).replace('{company}', company)
            send_email(service, 'me', email, "Quick Note", personalized_message)
            time.sleep(10)  # delay between each email


if __name__ == '__main__':
    main()
