import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Tony'
email['to'] = 'EMAILS'
email['subject'] = 'Hey there good looking!'

email.set_content("Whaaaat ya got coooking!?")

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('EMAILS', 'PASSWORD')
    smtp.send_message(email)
    print("email sent")
