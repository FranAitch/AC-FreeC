import smtplib, datetime, shelve, sys, anydbm, sendMail
anydbm._defaultmod = __import__('dumbdbm')
#anydb part added bc otherwise shelve causes an error when loaded via LaunchControl, dunno why

date = datetime.datetime.now()
thisMonth = date.month

shelfFile = shelve.open('monthlyMail')
lastMonth = shelfFile['lastMonth']

if lastMonth == thisMonth:
    shelfFile.close()
    sys.exit()

else:
    subject = ""      # CUSTOMIZE THESE VARIABLES
    message = ""      #  
    signoff = ""      # (You can leave this empty if you don't need to add to your message (see below))

# in my case, I need to add a line to my message every three months, uncomment and customize if you do too
#    if thisMonth == (10 or 1 or 4 or 7):       # customize months with different message
#        message += ""                          # add line(s)
    body = message + signoff
    
    sendMail(subject, body):
    shelfFile['lastMonth'] = thisMonth
    shelfFile.close()

