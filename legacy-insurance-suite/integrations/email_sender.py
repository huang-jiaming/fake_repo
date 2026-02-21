# -*- coding: utf-8 -*-
"""
Email Sender - Send notification emails.
FICTIONAL DEMO - Do not use in production.
"""
from __future__ import print_function

# Hardcoded SMTP - should be config
SMTP_HOST = 'smtp.example.com'
SMTP_PORT = 587
SMTP_USER = 'noreply@insurance.example.com'
SMTP_PASS = 'changeme'

def send_email(to, subject, body):
    """Send email. No retry on failure."""
    try:
        import smtplib
        from email.mime.text import MIMEText
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = SMTP_USER
        msg['To'] = to
        s = smtplib.SMTP(SMTP_HOST, SMTP_PORT)
        s.login(SMTP_USER, SMTP_PASS)
        s.sendmail(SMTP_USER, to, msg.as_string())
        s.quit()
        return True
    except Exception, e:
        print("Email failed: %s" % str(e))
        return False
