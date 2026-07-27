# 🤖 AI Auto-Reply Bot

An AI-powered auto-reply bot built with **Python**, **Google Gemini**, and **PyAutoGUI**. The bot monitors a chat, detects new incoming messages, generates context-aware responses using Gemini, and automatically sends the reply.

> **Disclaimer:** This project is intended for educational and learning purposes only. Automating messaging applications may violate the platform's Terms of Service. Use responsibly and at your own risk.

---

## ✨ Features

- 📩 Detects new incoming messages automatically
- 🤖 Generates intelligent replies using Google Gemini
- 🌐 Supports English, Hindi, and Hinglish conversations
- 💬 Maintains conversation context for natural responses
- 🚫 Prevents duplicate replies
- ⚡ Automatically pastes and sends responses
- 🔄 Continuously monitors the chat for new messages

---

## 🛠️ Tech Stack

- Python 3.x
- Google Gemini API
- PyAutoGUI
- Pyperclip
- python-dotenv

---

## 📂 Project Structure

```
AI-WhatsApp-AutoReply/
│
├── main.py
├── .env
├── requirements.txt
├── README.md
└── screenshots/
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/AI-WhatsApp-AutoReply.git
cd AI-WhatsApp-AutoReply
```

### 2. Create a virtual environment

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Configure Gemini API

Create a `.env` file in the project root.

```env
GEMINI_API_KEY=YOUR_API_KEY
```

---

## ▶️ Usage

1. Open **WhatsApp Web** or **WhatsApp Desktop**.
2. Open the chat you want the bot to monitor.
3. Update the mouse coordinates inside the script according to your screen resolution.
4. Run:

```bash
python main.py
```

The bot will:

- Select the visible chat
- Copy the conversation
- Detect new incoming messages
- Generate an AI response using Gemini
- Paste and send the reply automatically

---

## 🧠 How It Works

```
Loop
   │
   ▼
Select Chat
   │
   ▼
Copy Conversation
   │
   ▼
Extract Latest Message
   │
   ▼
Already Processed?
   │
 ┌─Yes──────────────┐
 │                  │
 Continue       No  ▼
              Check Sender
                   │
             Is New Message?
                   │
          No ──────┘
                   │
                  Yes
                   ▼
Generate Reply (Gemini)
                   │
                   ▼
Copy Reply
                   │
                   ▼
Paste & Send
```

---

## 📌 Key Logic

- Continuously monitors the conversation.
- Tracks the last processed message.
- Replies only when a **new incoming message** is detected.
- Uses Gemini to generate contextual replies.
- Prevents duplicate responses.

---

## 📷 Demo

Add screenshots or a GIF here.

Example:

```
screenshots/demo.gif
```

---

## 🚀 Future Improvements

- GUI using Tkinter or CustomTkinter
- Streamlit dashboard
- Multi-chat support
- Custom AI personalities
- Voice notifications
- Logging system
- Conversation history database
- Better message detection without UI selection
- Configurable reply styles
- Docker support

---

## 📚 Learning Outcomes

Through this project I learned:

- Python automation
- Prompt engineering
- Google Gemini API integration
- Clipboard management
- UI automation with PyAutoGUI
- State management
- Debugging real-world automation challenges

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome.

Feel free to fork the repository and submit a pull request.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Saksham Semwal**

GitHub: https://github.com/sakshamsemwal10

If you found this project helpful, consider giving it a ⭐ on GitHub!
