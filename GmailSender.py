from email.message import EmailMessage

""" email is a package, message is a module in email package, EmailMessage is a class with in the message module """

from security import password

import ssl
import smtplib

email_sender = "sagarkatnam@gmail.com"
email_password = password
email_receiver = "sagarkatnam@gmail.com"

email_subject = "In Cricket"

email_body = """

King = Virat Kohli
Alien/Mr.360 = Abraham Benjamin de Villiers
God = Sachin Tendulkar

Fact : Virat Kohli is the GREATEST OF ALL TIME 🐐
"""

em = EmailMessage()

em["From"] = email_sender
em["To"] = email_receiver
em["Subject"] = email_subject
em.set_content(email_body)

context = ssl.create_default_context()
"""ssl.create_default_context() is to create a secure SSL (Secure Sockets Layer) context, which is essential for establishing a secure connection when sending an email via an SMTP server."""

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
