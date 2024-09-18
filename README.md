# Python WhatsApp Bot 

## Project Description:
This WhatsApp bot, developed in Python, uses Flask and Twilio's API to receive messages via WhatsApp, perform Google searches, and return the first three unique results. The bot ensures that the results come from different domains and sends a header message before delivering the search results.

## Prerequisites:
- Python 3.9 or newer.
- A Twilio account with **Account SID** and **Auth Token**.
- The following Python libraries need to be installed:
  - Flask
  - Twilio
  - Flask-CORS
  - Google Search (`googlesearch-python`)
  - urllib

## Installation:

### 1. Clone the project:
Clone the project onto your computer:
```bash
git clone <project_url>
cd <project_name>
```

### 2. Create a virtual environment:
Create and activate a virtual environment for the project:
```bash
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

### 3. Install dependencies:
Install the required libraries to run the bot:
```bash
pip install flask twilio flask-cors googlesearch-python
```

### 4. Configure Twilio:
- Retrieve your **Account SID** and **Auth Token** from your [Twilio account](https://www.twilio.com/console).
- Enter these credentials in the code:
  ```python
  account_sid = 'your_account_sid'
  auth_token = 'your_auth_token'
  ```

### 5. Run ngrok:
The bot runs locally but must be accessible via the Internet for Twilio to send messages. Use ngrok to create a public URL:
```bash
ngrok http 5001
```

A public URL will be generated (e.g., `https://abcd1234.ngrok.io`). Copy this URL.

### 6. Configure Twilio to receive WhatsApp messages:
- Go to Twilio's console, in the **Programmable Messaging** > **WhatsApp Sandbox** section.
- Update the message reception URL with the generated ngrok URL, appending `/bot` to the end. For example:
```
https://abcd1234.ngrok.io/bot
```

### 7. Start the bot:
Run the Python script to start the bot:
```bash
python main.py
```

### 8. Test the bot:
- Send a message to your WhatsApp bot. For example: **"Python tutorial"**.
- The bot will perform a Google search and return three unique results as links, preceded by a header message such as **"--- Results for 'Python tutorial' ---"**.

## Features:
1. **Receiving messages via WhatsApp**: The bot receives WhatsApp messages through Twilio.
2. **Google Search**: The bot uses `googlesearch-python` to fetch the first three Google search results.
3. **Domain filtering**: Results are always from three different domains.
4. **Message order**: The bot sends a header message first, followed by the results in separate messages.
5. **Message sending**: Messages are sent using Twilio's API.