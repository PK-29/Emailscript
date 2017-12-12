import base64
import email
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def SendEmail(ToEmail, Ticketnum, Name):

    fromaddr = "princekowserr@gmail.com"
    toaddr = ToEmail
    msg = MIMEMultipart()
    msg['From'] = email.utils.formataddr(('Test', fromaddr))
    msg['To'] = toaddr
    msg['Subject'] = "Email Script"

    body = Ticketnum + " Me n My dawg " + Name
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)

    #encrupts data sent over
    server.starttls()
    server.ehlo()


    server.login(fromaddr, base64.b64decode("c3VwZXJtYW4yOQ=="))
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.set_debuglevel(True)  # show communication with the server
    server.quit()

if __name__ == "__main__":
    SendEmail("patelh11@mcmaster.ca", "20123", "CapPrice")
