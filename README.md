# SMTP Protocol Demo

A Python-based educational tool demonstrating the Simple Mail Transfer Protocol (SMTP). It features a graphical user interface (GUI) built with Tkinter, allowing users to connect to an SMTP server and send emails by manually interacting with the protocol.

![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)

---

## 📋 Features

- **GUI and CLI**: Includes a full-featured GUI (`GUI_SMTP.py`) and a core logic script (`SMTP_Logic.py`) for learning.
- **Manual SMTP Commands**: Interact directly using `EHLO`, `MAIL FROM`, `RCPT TO`, and `DATA` commands.
- **Real-time Log**: The GUI shows the full SMTP conversation, making it perfect for debugging and understanding the protocol.
- **Dark Theme**: A soft black, white, and green interface.
- **Threaded Operations**: Non-blocking connection and sending.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.6 or higher.
- Tkinter (usually included with standard Python installations).

### Installation
1.  **Clone the repository**:
    ```bash
    git clone https://github.com/ErfanShahbazzadeh/smtp-protocol-demo.git
    cd smtp-protocol-demo
    ```
2.  **(Optional) Create and activate a virtual environment**:
    ```bash
    # On Windows
    python -m venv venv
    venv\Scripts\activate

    # On macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```
3.  **Install dependencies**:
    No external libraries are required. Tkinter is part of Python's standard library.

---

## 💻 Usage

### Running the GUI
1.  Execute the main application script:
    ```bash
    python GUI_SMTP.py
    ```
2.  **Enter server details**: Enter the mail server of your choice.
3.  **Click "Connect"** to establish a connection.
4.  **Fill in email fields**: `From`, `To`, `Subject`, and your `Message Body`.
5.  **Click "Send Email"** to transmit the message.
6.  Observe the **Connection Log** at the bottom of the application to see the raw SMTP conversation.

### Using the Logic Module
For a non-GUI approach or to test the core functionality, you can import the class from `SMTP_Logic.py` in your own script.
```python
from SMTP_Logic import SMTPClient

client = SMTPClient("Your mail server", 25)
client.connect()
client.send_email("you@example.com", "friend@example.com", "Hello", "This is a test.")
```

---

## ⚙️ How It Works

This tool follows a standard SMTP session flow:
1.  **Connection**: Opens a TCP socket to the specified server.
2.  **Handshake**: Sends an `EHLO` command to identify itself.
3.  **Envelope**: Specifies the sender (`MAIL FROM`) and recipient (`RCPT TO`).
4.  **Transmission**: Sends the `DATA` command, followed by the email headers (From, To, Subject) and body.
5.  **Termination**: Ends the message with a solitary `.` and closes the session with `QUIT`.

---
## Screenshot

```
┌──────────────────────────────────────────────┐
│         ✉ SMTP Email Client                 │
│                                              │
│  Server: [  mail server  ] Port: [25]        │
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
│  │ 220 mail server ESMTP Ready          │    │
│  │ ✓ Email sent successfully!           │    │
│  └──────────────────────────────────────┘    │
└──────────────────────────────────────────────┘
```
---

## ⚠️ Important Notes

- **Educational Purpose**: This project is designed for learning the SMTP protocol. It implements a basic, unauthenticated SMTP session.
- **Server Authentication**: Many modern servers (like Gmail) require authentication (AUTH LOGIN). This tool works best with local or dedicated test servers.
- **Network Restrictions**: ISPs often block outbound traffic on port 25 to prevent spam. If you can't connect, try an alternative port like 587, or use a local test server.

---

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for details.
