import smtplib
from email.message import EmailMessage
from pathlib import Path
from string import Template

html = Template(Path('index.html').read_text())

email = EmailMessage()
email['from'] = 'your-email'
email['to'] = 'recipient-email'
email['subject'] = 'subject!'

email.set_content(html.substitute({'var': 'Dynamic content'}), 'html')  # or dict

with smtplib.SMTP(host='host mail', port=587) as smtp:
    # hello to server
    smtp.ehlo()
    # encryption
    smtp.starttls()
    smtp.login('email-address', 'smtp api password')  # get password from your email host
    smtp.send_message(email)
    print('Message sent')
