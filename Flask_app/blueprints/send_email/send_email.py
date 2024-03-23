from flask import Blueprint, request, session
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


send_email_bp = Blueprint('send_email', __name__)

@send_email_bp.route('/send_email', methods=['POST'])
def send_email():
    json_response = request.json
    email_body = json_response.get("email_body")
    email_title = json_response.get("email_title")

    # handle translation here? [KIV]
    smtp_server = 'smtp-mail.outlook.com'
    smtp_port = 587
    smtp_username = 'gpt10.4213.1@outlook.com' # dotenv() to load in main.py?
    smtp_password = 'gpt10email'

    from_email = 'gpt10.4213.1@outlook.com'
    # Assume emails are in session["email_list"]
    # to_email_list = session.get("email_list", None) # get email list from session, # Ensure not None
    to_email_list = ['gpt10.4213.1@outlook.com',] # Placeholder

    # meeting_date = "5/3/2024"
    # subject = f"{meeting_date} Meeting Minutes"  # meeting_date either user input or LLM search through document.
    subject = email_title
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = ", ".join(to_email_list) # send to multiple users
    msg['Subject'] = subject
    msg.attach(MIMEText(email_body))

    with smtplib.SMTP(smtp_server, smtp_port) as smtp:
        smtp.starttls()
        smtp.login(smtp_username, smtp_password)
        smtp.send_message(msg)

    return "Email sent successfully"