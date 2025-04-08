import base64
import mimetypes
import os
from email.message import EmailMessage

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.send']


def authentication():
    credentials = None

    if os.path.exists('token.json'):
        try:
            credentials = Credentials.from_authorized_user_file('token.json', SCOPES)
        except Exception as e:
            print("Failed to load token.json, forcing re-authentication.")
            credentials = None

    if not credentials or not credentials.valid:
        try:
            if credentials and credentials.expired and credentials.refresh_token:
                credentials.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file('client_secrets.json', SCOPES)
                credentials = flow.run_local_server(port=0)

            # Save the credentials
            with open('token.json', 'w') as token:
                token.write(credentials.to_json())

        except Exception as e:
            print(f"Authentication failed: {e}")
            exit(1)

    return credentials


def prepare_and_send_email(recipient, subject, message_text, attachment=None):
    credentials = authentication()

    try:
        service = build(serviceName='gmail', version='v1', credentials=credentials)
        message = create_message('aaryansharma1903@gmail.com', recipient, subject, message_text, attachment)
        send_message(service, 'me', message)
    except HttpError as error:
        print(f"An error occurred while sending the email: {error}")


def create_message(sender, to, subject, message_text, attachment=None):
    mime_message = EmailMessage()

    mime_message['From'] = sender
    mime_message['To'] = to
    mime_message['Subject'] = subject
    mime_message.set_content(message_text)

    if attachment:
        if not os.path.isfile(attachment):
            raise FileNotFoundError(f"Attachment file '{attachment}' not found.")
        type_subtype, _ = mimetypes.guess_type(attachment)
        if type_subtype is None:
            type_subtype = 'application/octet-stream'
        maintype, subtype = type_subtype.split('/')

        with open(attachment, 'rb') as fp:
            attachment_data = fp.read()

        mime_message.add_attachment(attachment_data, maintype, subtype, filename=os.path.basename(attachment))

    return {'raw': base64.urlsafe_b64encode(mime_message.as_bytes()).decode()}


def send_message(service, user_id, message):
    try:
        message = service.users().messages().send(userId=user_id, body=message).execute()
        print(f"✅ Message sent! ID: {message['id']}")
        return message
    except HttpError as error:
        print(f"An error occurred: {error}")


if __name__ == "__main__":
    # You can pass None here if you want no attachment
    prepare_and_send_email('user@gmail.com', 'Greeting from Aaryan', 'This is a test email', None)
    # prepare_and_send_email('justvs48@gmail.com', 'Greeting from Aaryan', 'This is a test email', 'test.txt') //to send with aattachment
