#!/usr/bin/env python
import sys
import imaplib
import getpass

username = 'chemila@gmail.com'
password = getpass.getpass()

server = 'imap.gmail.com'

gmail = imaplib.IMAP4_SSL(server)

print gmail.login(username, password)
#print gmail.login_cram_md5(username, password)
print gmail.select('INBOX')

typ, data = gmail.search(None, 'ALL')

for msg_id in data[0].split():
    typ, data = gmail.fetch(msg_id, '(RFC822)')
    print 'Message %s\n%s\n' % (msg_id, data[0][1])

gmail.close()
gmail.logout()
