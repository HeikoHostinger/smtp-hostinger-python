import smtp_hostinger

smtp = smtp_hostinger.SmtpHostinger()
smtp.auth("sender@hostinger.com", "Password123", "smtp.hostinger.com", 465, False)
smtp.send("recipient@hostinger.com", "sender@hostinger.com", "This means that emails work", "Message body...")