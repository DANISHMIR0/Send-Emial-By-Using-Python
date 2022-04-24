import smtplib
from email.message import EmailMessage

Message = EmailMessage()
print('''
╭━━━╮╱╱╱╱╱╱╭━━━╮╱╱╱╱╱╱╭╮╱╭━━━╮╱╱╱╱╱╱╱╭╮
╰╮╭╮┃╱╱╱╱╱╱┃╭━━╯╱╱╱╱╱╱┃┃╱┃╭━╮┃╱╱╱╱╱╱╱┃┃
╱┃┃┃┣━━┳━╮╱┃╰━━┳╮╭┳━━┳┫┃╱┃╰━━┳━━┳━╮╭━╯┣━━┳━╮
╱┃┃┃┃╭╮┃╭╮╮┃╭━━┫╰╯┃╭╮┣┫┃╱╰━━╮┃┃━┫╭╮┫╭╮┃┃━┫╭╯
╭╯╰╯┃╭╮┃┃┃┃┃╰━━┫┃┃┃╭╮┃┃╰╮┃╰━╯┃┃━┫┃┃┃╰╯┃┃━┫┃
╰━━━┻╯╰┻╯╰╯╰━━━┻┻┻┻╯╰┻┻━╯╰━━━┻━━┻╯╰┻━━┻━━┻╯''')
Message['TO'] = input("Plz Enter the Email Where Do u Want to sent : ")
Message['From'] = input("Plz Enter From option: ")
Message['Subject'] = input("Plz Enter the Subject: ")
Input_Message = input('Plz Enter the Message here: ')

Message.set_content(Input_Message)
From_which_Email = input('Enter the Email From U want to Send : ')
From_which_Email_Pwd = input("Enter the Email's Password From U Want To Send : ")
print("Sending..")
server = smtplib.SMTP_SSL('smtp.gmail.com',465)
server.login(From_which_Email,From_which_Email_Pwd)
server.send_message(Message)
print("Mail Sent")
server.quit()

#justfortestpurpose300@gmail.com','Qwerty@12345