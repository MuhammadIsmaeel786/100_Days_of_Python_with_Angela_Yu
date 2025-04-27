import smtplib
import os
from twilio.rest import Client
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class NotificationManager:

    def __init__(self):
        # Retrieve environment variables only once
        self.smtp_address = os.environ["EMAIL_PROVIDER_SMTP_ADDRESS"]
        self.email = os.environ["MY_EMAIL"]
        self.email_password = os.environ["MY_EMAIL_PASSWORD"]
        self.twilio_virtual_number = os.environ["TWILIO_VIRTUAL_NUMBER"]
        self.twilio_verified_number = os.environ["TWILIO_VERIFIED_NUMBER"]
        self.whatsapp_number = os.environ["TWILIO_WHATSAPP_NUMBER"]
        # Set up Twilio Client and SMTP connection
        self.client = Client(os.environ['TWILIO_SID'], os.environ["TWILIO_AUTH_TOKEN"])
        self.connection = smtplib.SMTP(self.smtp_address, 587)

    def send_sms(self, message_body):
        """
        Sends an SMS message through the Twilio API.
        """
        message = self.client.messages.create(
            from_=self.twilio_virtual_number,
            body=message_body,
            to=self.twilio_verified_number
        )
        # Prints if successfully sent.
        print(f"SMS sent with SID: {message.sid}")

    def send_whatsapp(self, message_body):
        """
        Sends a WhatsApp message through the Twilio API.
        """
        message = self.client.messages.create(
            from_=f'whatsapp:{self.whatsapp_number}',
            body=message_body,
            to=f'whatsapp:{self.twilio_verified_number}'
        )
        print(f"WhatsApp message sent with SID: {message.sid}")

    def send_emails(self, email_list, email_body):
        """
        Sends an email to a list of email addresses.
        """
        try:
            # Establish connection to the SMTP server
            self.connection.connect(self.smtp_address, 587)  # Explicitly connect
            self.connection.starttls()
            self.connection.login(self.email, self.email_password)

            # Send email to each recipient in the email list
            for email in email_list:
                self.connection.sendmail(
                    from_addr=self.email,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{email_body}".encode('utf-8')
                )
        except Exception as e:
            print(f"Error while sending email: {e}")
        finally:
            # Ensure that the connection is properly closed
            self.connection.quit()

