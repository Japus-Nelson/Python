import os
from PIL import Image
import smtplib
from email.message import EmailMessage
from tkinter import *
from tkinter import messagebox
from string import Template
from pathlib import Path
import imghdr

user_mail = 'japusnelson@gmail.com'
app_pass = 'bcoyajqpqrvrugty'
Rec_mail = 'japusjapus1134@gmail.com'
# File_name = Template(Path('thumbnail.jpg').read_text())

email = EmailMessage()
email["From"] = 'japusnelson@gmail.com'                         #os.environ.get('Python')
email["To"] = Rec_mail
email["Subject"] = 'Mail from Python With Multiple Attachment!!!'
email.set_content(f'Hey Buddy!! Congrats, This message has been sent from Python ')


# Im = ['thumbnail.jpg', 'unsplash.jpg']
pdf_files = ['wtr.pdf', 'wtr1.pdf', 'text', 'thumbnail.jpg', 'unsplash.jpg']
for pdf in pdf_files:
    with open(pdf, 'rb') as img:
    #read the files
        file_data = img.read()
        # file_type = imghdr.what(img)
     #Fetch the name of the file
        file_name = img.name
        print(file_data)
        # print(file_type)
        print(file_name)

        email.add_attachment(file_data, maintype = 'application', subtype='octet_stream', filename= file_name)
        # email.add_alternative('html document', subtype= 'html')

#connect to the smtp mail server to send mails:
with smtplib.SMTP(host='smtp.gmail.com', port=587) as mail:
    mail.ehlo()
    mail.starttls()
    mail.login(user_mail, app_pass)
    mail.send_message(email)
    mail.close()
    print('Mail sent!!')

