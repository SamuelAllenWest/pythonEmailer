
# Library built around email interactions
import smtplib

# Send Email will send the written email whenever we invoke the function

# Variable declarations
senderEmail = input('What email address would you like to send form?')
senderPassword = input('What is that email addresses app password?')
recipientEmail = input('What email address are we sending an email to?')
msg = input('What text would you like to send?')

# Send Email Function


def sendEmail(senderEmail, senderPassword, recipientEmail, msg):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    # SMPT taking in the  host and the port we're sending the email with
    # Initiate tls server from gmail account

    server.starttls()
    # login is what email we're sending from
    # Required use of an app password otherwise failed to login

    server.login(senderEmail, senderPassword)
    server.sendmail(senderEmail,
                    recipientEmail, msg)
    server.close()


sendEmail(senderEmail, senderPassword, recipientEmail, msg)
