import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['From'] = 'Jimwell Gersalia'
email['To'] = 'jimwellgersalia@gmail.com'
email['Subject'] = 'Change From'

email.set_content('I am a python master!')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('devops.jimwell@gmail.com', 'mytp qimn sjjn zxri')
    smtp.send_message(email)
    print('Email sent!')
