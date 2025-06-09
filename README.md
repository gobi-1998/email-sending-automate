# Gmail Auto Email Sender (Personalized Outreach Tool)

This is a **Python-based automation tool** that sends **personalized emails** to a list of contacts using the **Gmail API (OAuth 2.0)**.

---

## 💡 What It Does

* Reads contacts from a CSV file (`contacts.csv`)
* Reads a message template from `message.txt`
* Uses Gmail API with OAuth 2.0 to send emails securely
* Adds a **10-second delay** between emails
* Prompts for **confirmation before sending each email**
* Helps automate professional or job-seeking outreach

---

## 🔧 Setup Instructions

### 1. Set Up Google Cloud OAuth Credentials

1. Visit the [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project
3. Enable the **Gmail API**
4. Go to **APIs & Services > Credentials > Create Credentials > OAuth client ID**
5. Choose **Desktop App** and download the `credentials.json` file
6. Place `credentials.json` in the root folder of this project
   ⚠️ Do **not** upload this file to GitHub

---

### 2. Install Python Dependencies

Install the required packages using pip:

```bash
pip install --upgrade google-auth google-auth-oauthlib google-api-python-client
```

---

### 3. Create Required Files

#### `contacts.csv`

This file should contain the list of people you want to email.
Create a CSV file with the following headers:

```csv
Name,Email,Company
Anu,anu@example.com,Wells Fargo
Gobi,gobi@example.com,Self
```

* **Name**: The recipient’s first name
* **Email**: The email address
* **Company**: Their company or organization (used in message personalization)

The script will use this CSV to send personalized messages using the `Name` and `Company` fields.

---

#### `message.txt`

Create a plain text file with your email message.
Use `{name}` and `{company}` as placeholders for personalization:

```txt
Hi {name},

I hope you're doing well. Apologies for reaching out directly. I came across your profile and was genuinely inspired by your work at {company}.

I'm currently exploring opportunities in AI and backend engineering, and I’d really value the chance to ask you a referral or share my resume for any feedback or guidance.

Of course, if that’s not possible, I completely understand — I’d still truly appreciate any insights you could share. And if my message caused any inconvenience, I sincerely apologize.

Warm regards,
```

> 🔁 The code reads this file and replaces `{name}` and `{company}` for each contact row automatically.

---

### 4. Run the Script

```bash
python email_automation.py
```

The script will:

* Ask for your Gmail OAuth approval (on first run)
* Load your contact list
* Personalize the message for each row
* Ask: `Send email to [name] <email>? (yes/no)`
* Wait 10 seconds between each email

---

## ⚠️ Important

* **Never share `credentials.json` or `token.pickle`**
* Always respect email etiquette and avoid spammy behavior
* This script is for **personal, ethical outreach** (e.g., referrals, mentorship)

---

## 🙌 Contribute & Improve

Ideas, improvements, and pull requests are welcome!
Feel free to fork this repo and build your own version!
