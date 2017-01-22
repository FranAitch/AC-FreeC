# NOTE this is customized for gmail addresses, for others you'll have to alter the SMTP data
import smtplib

myMailAddress = ""      # set to your mail address
myPassWord = ""         # set to your password
mailRecipients = None   # set to either a string with one address or a list of strings for several recipients

def sendMail(subject, message):
    """send myself an email, providing a subject and a message"""

    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)   #TODO catch connection errors
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login(myMailAddress, myPassWord)        # TODO check if return startswith (235)
    smtpObj.sendmail(myMailAddress, mailRecipients, 'Subject: {}\n\n{}' .format(subject, message))
    # NOTE for some reason, body only appears with TWO newline characters
    smtpObj.quit()
