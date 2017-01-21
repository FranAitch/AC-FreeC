# NOTE this is customized for gmail addresses, for others you'll have to alter the SMTP data
import smtplib

myMailAddress = None   # set to your mail address (string value)
myPassWord = None      # set to your password  (string value)

def sendMail(subject, message):
    """send myself an email, providing a subject and a message"""

    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)   #TODO catch connection errors
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login(myMailAddress, myPassWord)        # TODO check if return startswith (235)
    smtpObj.sendmail(myMailAddress, myMailAddress, 'Subject: {}\n\n{}' .format(subject, message))
    # NOTE for some reason, body only appears with TWO newline characters
    smtpObj.quit()
