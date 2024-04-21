import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Jimwell Gersalia'
email['to'] = 'jimwelldeveloper@gmail.com'
email['subject'] = 'Change from'

email.set_content(html.substitute({'name': 'Mary Joy'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('devops.jimwell@gmail.com', 'mytp qimn sjjn zxri')
    smtp.send_message(email)
    print('Email Sent!')
