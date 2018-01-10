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


def SendEmail(ToEmail, Name, Ticketnum):
    # check if email syntax is right
    addressToVerify = ToEmail
    match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', addressToVerify)

    if match == None:
        print('Bad Syntax')
        return "Incorrect Email"
        #raise ValueError('Bad Syntax')

    # # Step 2: Getting MX record
    # # Pull domain name from email address
    # domain_name = addressToVerify.split('@')[1]
    #
    # # get the MX record for the domain
    # records = dns.resolver.query(domain_name, 'MX')
    # mxRecord = records[0].exchange
    # mxRecord = str(mxRecord)
    #
    # # Step 3: ping email server
    # # check if the email address exists
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
    #     print('Y')
    # else:
    #     print('N')

    fromaddr = "lyons.newmedia@gmail.com"
    toaddr = ToEmail
    msg = MIMEMultipart()
    msg['From'] = email.utils.formataddr(('Lyons Newmedia', fromaddr))
    msg['To'] = toaddr
    msg['Subject'] = "3D Print Request - Ready for Pickup"

    body = "Hi "+ color.BOLD + Name + ",\n\nGood news! The following requested 3D print job has been printed successfully:\n\n" + "Ticket '#': " + Ticketnum + "\n\nPlease bring this email and your McMaster ID card with you to the Help Desk in Lyons New Media Centre (Mills Library, 4th floor) to retrieve your item.\n\nYou will be required to sign for it, so a proxy cannot come to pick this up for you.\n\nWe will hold this item for no more than 30 days from today's date before it is reclaimed and/or recycled.  If you cannot make it into the Centre due to work/being home etc., please let us know and we can arrange to hold onto it until you can make it in.\n\nSincerely,\n\nLyons New Media Centre Staff\n\n--\nLyons New Media Centre\n4th Floor, Mills Library"
    html = """\
    <html>
      <head></head>
      <body>
        <p>Hi <b>"""+Name+"""</b><br><br>
           Good news! The following requested 3D print job has been printed successfully:<br><br>
           <mark><b>Ticket#: """+ Ticketnum +"""</b></mark><br><br>
           Please bring this email and your McMaster ID card with you to the Help Desk in Lyons New Media Centre (Mills Library, 4th floor) to retrieve your item.<br><br>
           You will be required to sign for it, so a proxy cannot come to pick this up for you.<br><br>
           We will hold this item for no more than 30 days from today's date before it is reclaimed and/or recycled.  If you cannot make it into the Centre due to work/being home etc., please let us know and we can arrange to hold onto it until you can make it in.<br><br>
           Sincerely,<br><br>
           <i>Lyons New Media Centre</i><br><br>
           --<br>
           Lyons New Media Centre<br>
           4th Floor, Mills Library<br>
           <a href="library.mcmaster.ca/lyons">library.mcmaster.ca/lyons</a>
        </p>
      </body>
    </html>
    """
    msg.attach(MIMEText(html, 'html'))

    server = smtplib.SMTP('smtp.gmail.com', 587)

    #encrupts data sent over
    server.starttls()
    server.ehlo()


    server.login(fromaddr, base64.b64decode("Q3IzNHQxdjNNMW5kcw=="))
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.set_debuglevel(True)  # show communication with the server
    server.quit()
    return ("Email SENT")

if __name__ == "__main__":

     print SendEmail("princekowserr@gmail.com","TEST","20202")
     #body = "Hi " + color.BOLD + "PRice" + " ,Good news! The following requested 3D print job has been printed successfully:\n\n" + "Ticket '#': " + "AS" + "\n\nPlease bring this email and your McMaster ID card with you to the Help Desk in Lyons New Media Centre (Mills Library, 4th floor) to retrieve your item.\n\nYou will be required to sign for it, so a proxy cannot come to pick this up for you.\n\nWe will hold this item for no more than 30 days from today's date before it is reclaimed and/or recycled.  If you cannot make it into the Centre due to work/being home etc., please let us know and we can arrange to hold onto it until you can make it in.\n\nSincerely,\n\nLyons New Media Centre Staff\n\n--\nLyons New Media Centre\n4th Floor, Mills Library"
     #print body