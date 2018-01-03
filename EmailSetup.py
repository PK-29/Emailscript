import base64
import email
import smtplib
import socket
import re
import dns.resolver
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def printye(ye):
    return "yeyeye"


def SendEmail(ToEmail, Ticketnum, Name):
    # check if email syntax is right
    addressToVerify = ToEmail
    match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', addressToVerify)

    if match == None:
        print('Bad Syntax')
        return "Incorrect Email"
        #raise ValueError('Bad Syntax')

    # Next we need to get the MX record for the target domain, in order to start the email verification process.
    records = dns.resolver.query('gmail.com', 'MX')
    mxRecord = records[0].exchange
    mxRecord = str(mxRecord)

    # Get local server hostname
    host = socket.gethostname()

    # SMTP lib setup (use debug level for full output)
    server = smtplib.SMTP()
    server.set_debuglevel(0)

    # SMTP Conversation
    server.connect(mxRecord)
    server.helo(host)
    server.mail('me@domain.com')
    code, message = server.rcpt(str(addressToVerify))
    server.quit()

    # Assume 250 as Success
    if code == 250:
        print('Success')
    else:
        print('Bad')
        return ("Incorrect Email")

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


    server.login(fromaddr, base64.b64decode("="))
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.set_debuglevel(True)  # show communication with the server
    server.quit()
    return ("Email SENT")

if __name__ == "__main__":

     for i in range(20):
        SendEmail("nguyenbh@mcmaster.ca", "20123", "CapPrice")
