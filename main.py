from flask import Flask, request
from googlesearch import search
from twilio.twiml.messaging_response import MessagingResponse
from flask_cors import CORS
from urllib.parse import urlparse  # To extract domains from URLs
from twilio.rest import Client  # To send a separate message
import os

app = Flask(__name__)
CORS(app)  # Allow external requests

# Configure your Twilio Account SID and Auth Token
account_sid = 'TWILIO_ACCOUNT_SID'  # Replace with your credentials
auth_token = 'TWILIO_AUTH_TOKEN'  # Replace with your credentials
client = Client(account_sid, auth_token)

# Function for the bot to handle WhatsApp requests
@app.route("/bot", methods=["POST"])
def bot():
    # Get the user's message
    incoming_msg = request.values.get('Body', '').lower()
    from_number = request.values.get('From')  # Sender's phone number (WhatsApp)
    to_number = request.values.get('To')  # Receiver's phone number (Twilio)

    # Create a Twilio response object
    response = MessagingResponse()

    # Bot logic: Google search
    if incoming_msg:
        query = incoming_msg  # Use the query without limiting it to a specific site
        result = []
        domains = set()  # Set to store unique domains

        # Perform Google search with a larger number of results (10)
        for i in search(query, num_results=10):
            # Extract the domain from the link
            domain = urlparse(i).netloc

            # Add only if the domain has not been encountered yet
            if domain not in domains:
                domains.add(domain)
                result.append(i)

            # Stop once we have 3 unique results
            if len(result) == 3:
                break

        # Always send the header first
        if result:
            # Send the header separately using Twilio API
            client.messages.create(
                body=f"--- Results for '{incoming_msg}' ---",
                from_=to_number,
                to=from_number
            )

            # Send each URL in a separate message
            for url in result:
                response.message(url)
        else:
            response.message("Sorry, no results found.")
    else:
        response.message("I didn't understand your request.")

    return str(response)

if __name__ == "__main__":
    # Run the Flask application
    app.run(host='0.0.0.0', port=5001, debug=True)
