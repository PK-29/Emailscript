import base64
import email
import smtplib
import socket
import re
import dns.resolver
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
class color:
    BOLD = '\033[1m'
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

    # # Next we need to get the MX record for the target domain, in order to start the email verification process.
    # records = dns.resolver.query('gmail.com', 'MX')
    # mxRecord = records[0].exchange
    # mxRecord = str(mxRecord)
    #
    # # Get local server hostname
    # host = socket.gethostname()
    #
    # # SMTP lib setup (use debug level for full output)
    # server = smtplib.SMTP()
    # server.set_debuglevel(0)
    #
    # # SMTP Conversation
    # server.connect(mxRecord)
    # server.helo(host)
    # server.mail('me@domain.com')
    # code, message = server.rcpt(str(addressToVerify))
    # server.quit()
    #
    # # Assume 250 as Success
    # if code == 250:
    #     print('Success')
    # else:
    #     print('Bad')
    #     return ("Incorrect Email")

    fromaddr = "lyons.newmedia@gmail.com"
    toaddr = ToEmail
    msg = MIMEMultipart()
    msg['From'] = email.utils.formataddr(('Lyons Newmedia', fromaddr))
    msg['To'] = toaddr
    msg['Subject'] = "3D Print Request - Ready for Pickup"

    body = "Hi "+ color.BOLD + Name + """ ,

        Good news! The following requested 3D print job has been printed successfully:

        """ + "\033[44;33mTicket '#': TICKETNUMBER\033[m" + """"

        Please bring this email and your McMaster ID card with you to the Help Desk in Lyons New Media Centre (Mills Library, 4th floor) to retrieve your item.

        You will be required to sign for it, so a proxy cannot come to pick this up for you.

        We will hold this item for no more than 30 days from today's date before it is reclaimed and/or recycled.  If you cannot make it into the Centre due to work/being home etc., please let us know and we can arrange to hold onto it until you can make it in.

        Sincerely,

        """ + "\033[3mLyons New Media Centre Staff\033[0m" + """
            
        --
        Lyons New Media Centre
        4th Floor, Mills Library
        """

 
    html = """\
    <html>
        <head></head>
        <body>
            <p><a href="library.mcmaster.ca/lyons"></a></p>
        </body>
    </html>
"""
    msg.attach(MIMEText(body, 'plain'))
    msg.attach(MIMEText(html, 'html'))

    server = smtplib.SMTP('smtp.gmail.com', 587)

    #encrupts data sent over
    server.starttls()
    server.ehlo()


    server.login(fromaddr, base64.b64decode("Q3IzNHQxdjNNMW5kcw="))
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.set_debuglevel(True)  # show communication with the server
    server.quit()
    return ("Email SENT")

if __name__ == "__main__":

     ##print SendEmail("pincekowserr@gmail.com","20026","TEST")
