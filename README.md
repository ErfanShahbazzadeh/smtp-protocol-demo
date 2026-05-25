Here's a simple README for your SMTP email client:

```markdown
# SMTP Email Client

A Python-based SMTP email client with a graphical user interface (GUI) built using Tkinter. This application allows you to connect to an SMTP server and send emails directly using the SMTP protocol.

---

## Features

- Connect to any SMTP server (default: `mail.uma.ac.ir`)
- Send emails with custom **From**, **To**, **Subject**, and **Body**
- Real-time SMTP conversation log
- Dark theme UI with green accents
- Non-blocking operations (threaded)
- Manual SMTP conversation for educational purposes

---

## Requirements

- Python 3.6 or higher
- Tkinter (comes pre-installed with Python on most systems)

No external libraries are required.

---

## Installation

1. Clone or download this repository
2. Make sure Python is installed:
   ```bash
   python --version
   ```
3. Run the script:
   ```bash
   python smtp_client.py
   ```

---

## Usage

1. **Enter server details** — SMTP server address and port (default: `mail.uma.ac.ir:25`)
2. **Click "Connect"** — connects to the SMTP server
3. **Fill in email details**:
   - **From** — sender's email address
   - **To** — recipient's email address
   - **Subject** — email subject line
   - **Message Body** — the content of your email
4. **Click "Send Email"** — sends the email via SMTP

The connection log at the bottom shows the full SMTP conversation for debugging and educational purposes.

---

## SMTP Commands Used

This client implements basic SMTP commands:
- `EHLO` — identify to the server
- `MAIL FROM` — specify sender
- `RCPT TO` — specify recipient
- `DATA` — begin message transmission
- `QUIT` — end session

---

## Notes

- Some SMTP servers may require authentication (AUTH LOGIN)
- Port 25 may be blocked by some ISPs; try port 587 if connection fails
- This tool is intended for **educational purposes** only

---

## Screenshot

```
┌──────────────────────────────────────────────┐
│         ✉ SMTP Email Client                  │
│                                              │
│  Server: [mail.uma.ac.ir    ] Port: [25]     │
│  [Connect]                                   │
│  ─────────────────────────────────────────   │
│  From:    [sender@example.com          ]     │
│  To:      [recipient@example.com       ]     │
│  Subject: [Test Email                  ]     │
│                                              │
│  Message Body:                               │
│  ┌──────────────────────────────────────┐    │
│  │ Hello,                               │    │
│  │ This is a test email.                │    │
│  │                                      │    │
│  └──────────────────────────────────────┘    │
│                                              │
│  [Send Email]                                │
│  Status: Connected                           │
│                                              │
│  Connection Log:                             │
│  ┌──────────────────────────────────────┐    │
│  │ 220 mail.uma.ac.ir ESMTP Ready       │    │
│  │ ✓ Email sent successfully!           │    │
│  └──────────────────────────────────────┘    │
└──────────────────────────────────────────────┘
```

---

## License

This project is for educational purposes.
```

---
