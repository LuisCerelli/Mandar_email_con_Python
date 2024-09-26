import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

your_email = 'xxxxxxxxxxxxxxxxxo@gmail.com'
your_password = 'xxxx xxxx xxxx xxxx'

recipent = 'cerluisalberto@gmail.com'

message = MIMEMultipart()
message['From'] = your_email
message['To'] = recipent
message['Subject'] = 'Email de agradecimiento'

body = 'Muchas gracias a todos por el apoyo! Se agradece mucho porque cada vez somos mas!!!'

message.attach(MIMEText(body, 'plain'))

smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
smtp_server.starttls()
smtp_server.login(your_email, your_password)

smtp_server.sendmail(your_email, recipent, message.as_string())
smtp_server.quit
print('Email enviado')

