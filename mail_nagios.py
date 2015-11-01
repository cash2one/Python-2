#!/usr/bin/env python
# encoding: utf-8
# mail -S "content..." to_addr1 to_addr2

import sys
import smtplib
from email.mime.text import MIMEText


para_to_addr    = [sys.argv[1]]
para_subject    = sys.argv[2]
para_content    = sys.argv[3]

print para_to_addr
print para_subject
print para_content


smtpserver      = 'smtp..163.com'
from_addr       = 'geektcp@163.com'
pwd             = "hello!@#CVB"

subject         = para_subject

msg             = MIMEText(para_content)

msg["Subject"]  = para_subject
msg["From"]     = from_addr
msg["To"]       = ",".join(para_to_addr)


s = smtplib.SMTP(smtpserver, timeout=30)
s.login(from_addr, pwd)
s.sendmail(from_addr, para_to_addr, msg.as_string())
s.close()
